from flask import Flask
from crawler.service.jobService import JobService
from dotenv import load_dotenv

load_dotenv()

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
        'error': False,
        'message': "Job Finish"
    }


@app.route("/api/job/process")
def process():
    print("Init Process")
    jobService = JobService()
    print("Start Process")
    jobService.process()

    print("Finish Process")
    return {
        'error': False,
        'message': "Process Finish"
    }


app.run(host="0.0.0.0", debug=True, port=5000)

# if __name__ == "__app__":
#     # Only for debugging while developing
#     app.run(host="0.0.0.0", debug=True, port=80)
