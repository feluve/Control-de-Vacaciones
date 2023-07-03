from django.shortcuts import render

# Create your views here.


def encuesta(request):
    print("Vista: encuesta", request.user)

    context = {}

    return render(request, "encuesta.html", context)
