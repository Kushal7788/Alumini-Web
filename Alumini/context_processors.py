from .models import *


def addVariableToContext(request):
    return {
        'contact_us': AluminiHome.objects.all(),
    }
