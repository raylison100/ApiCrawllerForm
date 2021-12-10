from django.http import JsonResponse
from ..service.jobService import JobService


def start(request):
    print("Init Job")
    jobService = JobService()
    print("Start Job")
    jobService.start()

    print("Finish Job")
    return JsonResponse(
        {
            'erro': False,
            'message': "Job Finish"
        }
    )


def healthz(request):
    return JsonResponse(
        {
            'error': False,
            'message': "API CRAWLER ON"
        }
    )
