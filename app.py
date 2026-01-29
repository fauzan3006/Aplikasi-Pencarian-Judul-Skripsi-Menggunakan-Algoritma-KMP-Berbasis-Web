from flask import Flask, render_template, request
import csv
import re

app = Flask(__name__)


def load_dataset():
    data = []
    with open(
    "dataset_skripsi_unismuh.csv",
    newline="",
    encoding="utf-8-sig"
) as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                "judul": row["judul"],
                "penulis": row["penulis"],
                "nim": row["nim"]
            })
    return data


dataset = load_dataset()


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(pattern, text):
    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return True
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False



def highlight(text, keyword):
    return re.sub(
        f"({re.escape(keyword)})",
        r"<span class='highlight'>\1</span>",
        text,
        flags=re.IGNORECASE
    )



@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    keyword = ""

    if request.method == "POST":
        keyword = request.form["keyword"].strip().lower()

        for item in dataset:
            if kmp_search(keyword, item["judul"].lower()):
                results.append({
                    "judul": highlight(item["judul"], keyword),
                    "penulis": item["penulis"],
                    "nim": item["nim"]
                })

    return render_template(
        "index.html",
        results=results,
        keyword=keyword,
        jumlah=len(results)
    )


if __name__ == "__main__":
    app.run(debug=True)
