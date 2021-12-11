# save this as app.py
from flask import Flask
from crawler.service.jobService import JobService

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/api/healthz")
def healthz():
    return {
        'error': False,
        'message': "API CRAWLER ON"
    }


@app.route("/api/job/start")
def start():
    print("Init Job")
    jobService = JobService()
    print("Start Job")
    jobService.start()

    print("Finish Job")
    return {
        'erro': False,
        'message': "Job Finish"
    }


if __name__ == "__app__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
