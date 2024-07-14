from django.shortcuts import render


def django(argument):
    return render(argument, 'django.html')