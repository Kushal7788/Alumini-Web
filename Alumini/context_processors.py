from .models import *


def addVariableToContext(request):
    if AluminiHome.objects.count():
        obj = AluminiHome.objects.get(id_no=1)
    else:
        obj = None
    return {
        'homedata': obj,
    }