from flask import Flask, request
import urllib.parse
import os
import threading

app = Flask(__name__)


def update(url):
    os.system(f"python gen_new.py --url {url}")


@app.route("/")
def update():
    try:
        url = request.get_data("url")
        url = url.decode("utf-8")
        url = urllib.parse.unquote(url)
        url = url.split("=")
        url = url[1]
        print(url)
        update_thread = threading.Thread(target=update, args=url)
        update_thread.start()
        return "hello"
    except:
        return "failed to get url"

