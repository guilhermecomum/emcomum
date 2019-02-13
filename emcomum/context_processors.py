from django.conf import settings

def ga_tracking(request):
    return {'ga_tracking': settings.GA_TRACKING}
