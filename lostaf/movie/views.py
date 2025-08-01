from django.shortcuts import render

def home(request):
    context = {'name': 'Greg Lim'}
    return render(request, 'home.html', context)

