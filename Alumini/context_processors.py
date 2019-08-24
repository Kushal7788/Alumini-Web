from .models import *


def addVariableToContext(request):
    return {
        'homedata': AluminiHome.objects.all,
    }