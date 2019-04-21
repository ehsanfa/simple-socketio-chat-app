from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis')

@app.route("/groups", methods=["GET", "POST"])
def groups():
	if request.method == "GET":
	    groups = r.hkeys("groups")
	    return jsonify([group.decode("utf-8") for group in groups])
	elif request.method == "POST":
		group_name = request.get_json()['form']["group_name"]
		group_slug = group_name.replace(" ", "_")
		r.hset("groups", group_slug, group_name)
		return jsonify({
			"status": 1	,
			"name": group_name,
			"slug": group_slug
		})
