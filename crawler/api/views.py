from django.http import JsonResponse
from ..service.jobService import JobService


def start(request):
    try:
        jobService = JobService()
        jobService.start()

        return JsonResponse(
            {
                'erro': False,
                'message': "Job Finish"
            }
        )
    except:
        return JsonResponse(
            {
                'erro': True,
                'message': "Job Fail"
            }
        )


def healthz(request):
    return JsonResponse(
        {
            'error': False,
            'message': "API CRAWLER ON"
        }
    )
