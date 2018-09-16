from django.shortcuts import render


def index(request):
    context = {'name': 'sammy'}
    return render(request, 'index.html', context)