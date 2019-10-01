# coding=utf-8
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import platform
import urllib.request as request
import requests

app = Flask(__name__)

# Running on root
@app.route("/")
def root():
    html = "<h1>Pond5 Code Test 2019 - Cláudia Correia</h1>\
        <p>GET /ping request should return “pong”</p>\
        <p>GET /system request should return JSON object with service version and system information.</p>\
        <p>GET /mediainfo/id should return a JSON object with image filename, size, dimensions and image title.</p>"
    return html


# Ping pond5 website // test the reachability of a host on an IP network
@app.route("/ping", methods=["GET"])
def ping():
    url = requests.get("https://www.pond5.com/")
    if url.status_code == 200:
        return "pong"
    else:
        return "unreachable"

# Return JSON object with service version and system information
@app.route("/system")
def system():
    sys_info = {
        "machine": platform.machine(),
        "version": platform.uname().version,
        "platform": platform.platform(),
        "system": platform.uname().system,
        "processor": platform.processor(),
    }
    return jsonify(sys_info)

# Return a JSON object with image filename, size, dimensions and image title
@app.route("/mediainfo/<id>", methods=["GET"])
def mediainfo(id):
    link = "https://www.pond5.com/photo/" + str(id)
    html_doc = request.urlopen(link)

    # Parse HTML doc 
    soup = BeautifulSoup(html_doc, 'html.parser')


    # property="og:image"
    filename = soup.find("meta", property="og:image")["content"]
    filename = filename.replace('https://images.pond5.com/','')
    # File Size:
    size = soup.find_all("dd")[12].text
    # property="og:image:height"
    height = soup.find("meta", property="og:image:height")["content"]
    # property="og:image:width"
    width = soup.find("meta", property="og:image:width")["content"]
    # property="twitter:title"
    title = soup.find("meta", property="twitter:title")["content"]

    # Dictionary to return JSON object with image filename, size, dimensions and image title
    json_info = {
        "filename": filename,
        "size": size,
        "height": height,
        "width": width,
        "title": title,
    }
    return jsonify(json_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
