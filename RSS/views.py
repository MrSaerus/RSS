from django.shortcuts import render

def show(request):
    name = "3.5"
    return render(request, 'face.html', locals())