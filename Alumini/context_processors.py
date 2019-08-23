from .models import *


def addVariableToContext(request):
    return {
        'homedata': AluminiHome.objects.get(id_no=1),
    }
