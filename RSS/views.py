from django.shortcuts import render

def show(request):
    title_page = "Читалка"
    name = "3.5"
    return render(request, 'face.html', locals())