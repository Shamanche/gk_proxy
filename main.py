# from urllib import request
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "It's OK"

@app.route('/', methods=['POST'])
def handler():
    print(request)
    return 200

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)



