from django.shortcuts import render  # type: ignore
# from django.http import HttpResponse  # type: ignore


def home(request):
    return render(request, 'todos/home.html')
