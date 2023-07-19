from django.shortcuts import render, redirect
from .models import *
from django.template.loader import render_to_string
from django.http import JsonResponse

def BASE(request):
    return render(request, 'base.html')


def home(request):
    categories = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('-id')
    context = {"category": categories, "course": course}
    return render(request, 'Main/home.html', context)


def singlecourse(request):
    category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    FreeCourse_count = Course.objects.filter(price = 0).count()
    PaidCourse_count = Course.objects.filter(price__gte=1).count()

    context = {
        'category':category,
        'level':level,
        'course':course,
        'FreeCourse_count':FreeCourse_count,
        'PaidCourse_count':PaidCourse_count,
    }
    return render(request, 'Main/singlecourse.html', context)

def filterdata(request):
    category = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['PriceFree']:
       course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
       course = Course.objects.filter(price__gte=1)
    elif price == ['PriceAll']:
       course = Course.objects.all()
    elif category:
        course = Course.objects.filter(category__id__in = category).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in = level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    context = {
        'course': course
    }
    t = render_to_string('ajax/course.html', context)
    return JsonResponse({'data': t})


def contactus(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category' : category
    }
    return render(request, 'Main/contactus.html', context)


def aboutus(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category' : category
    }

    return render(request, 'Main/aboutus.html', context)

def searchcourse(request):
    category = Categories.get_all_category(Categories)

    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    context = {
        'course' : course,
        'category': category
    }
    return render(request, 'search/search.html', context)

def coursedetails(request, slug):
    category = Categories.get_all_category(Categories)

    course = Course.objects.filter(slug = slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')

    context = {
        'course' : course,
        'category': category
    }
    return render(request, 'course/course_details.html', context)

def pagenotfound(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category' : category
    }
    return render(request, 'error/404.html', context)





