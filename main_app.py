from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = {}

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def post_task():
    data = request.get_json()
    tasks.update(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
