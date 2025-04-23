from flask import Flask, request, render_template, send_file
import pandas as pd
from utils import translate
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        sheet = request.form["sheet"]
        start = int(request.form["start"])
        end = int(request.form["end"])
        lang_col = request.form["lang_col"].strip().upper()

        df = pd.read_excel(file, sheet_name=sheet)
        block = df.iloc[start-1:end].copy()
        memory = {}

        for i in block.index:
            val = block.at[i, lang_col]
            if pd.isna(val) or val == "" or val == block.at[i, "ENG"] or val == block.at[i, "ITA"]:
                source = block.at[i, "ENG"] if pd.notna(block.at[i, "ENG"]) else block.at[i, "ITA"]
                block.at[i, lang_col] = translate(source, memory)

        output_path = f"translated_{start}_{end}.xlsx"
        block.to_excel(output_path, index=False)
        return send_file(output_path, as_attachment=True)

    return render_template("index.html")
