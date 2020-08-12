from flask import Flask, request
import urllib.parse
import os
import threading

app = Flask(__name__)


def update_flatpak(url):
    os.system(f"python gen_new.py --url {url}")


@app.route("/", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        url = request.form["url"]
        update_thread = threading.Thread(target=update_flatpak, args=(url,))
        update_thread.start()
        return "hello"
    else:
        return "hello"

