from flask import Flask, render_template, request
import os
import re

template_dir = os.path.dirname(__file__)
app = Flask(__name__, template_folder=template_dir)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        ip = request.form.get("ip")

        if re.match(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", ip) and not any(char in ip for char in [";", "|", "&", "/" "{", "}"]):
            cmd = "eval \"ping -c 4 " + ip + "\""
            print(cmd) #Tambahan
            result = os.popen(cmd).read()
            return render_template("index.html", **{"data": result})
        else:
            return render_template("index.html", **{"data": "NO HACKING ALLOWED!!!! >:("})


if __name__ == "__main__":
    app.run("0.0.0.0", port=9999)
