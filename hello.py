from flask import Flask, json, jsonify, render_template
import os, json, requests
app = Flask(__name__)

@app.route("/")
def index():
	#url = dockerurl
	#resoonse = json.loads(url)
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "data.json")
    json2_url = os.path.join(SITE_ROOT, "static/data", "second.json")
    data = json.load(open(json_url))
    data2 = json.load(open(json2_url))
    #print ((type(data)))
    #page = ('score:', data['predict']['predictscore']['score'])
    #print (type(page))
    print (data['predict'])
    scoresData = data['predict']['predictscore']
    print (scoresData)
    return  render_template(
        'index.html',
        data=data,
        data2=data2,
        scores = scoresData)

if __name__ == "__main__":
	app.run()