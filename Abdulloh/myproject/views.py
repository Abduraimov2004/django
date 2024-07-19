from django.shortcuts import render


def car(request):
    car_list = ["Toyota", "Honda", "Ford", "BMW", "Mercedes"]
    return render(request, 'car.html', {'car_list': car_list})


def companiy(request):
    company_list = ["Google", "Microsoft", "Apple", "Amazon", "Facebook"]
    return render(request, 'companiy.html', {'company_list': company_list})

def p_language(request):
    programming_language_list = ["Python", "Java", "C++", "JavaScript", "C#"]
    return render(request, 'prog_language.html', {'programming_language_list': programming_language_list})