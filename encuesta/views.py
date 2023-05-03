from django.shortcuts import render

# Create your views here.


def encuesta(request):
    
    context = {
        
    }
    
    return render(request, 'encuesta.html', context)