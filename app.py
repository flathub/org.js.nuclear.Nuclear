from flask import Flask, request
import urllib.parse
import os

app = Flask(__name__)


@app.route("/")
def update():
    url = request.get_data("url")
    url = url.decode("utf-8")
    url = urllib.parse.unquote(url)
    os.system(f"python gen_new.py --url {url}")
    return "hello"
