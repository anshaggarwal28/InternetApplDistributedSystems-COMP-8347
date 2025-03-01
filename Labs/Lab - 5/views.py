'''
from django.shortcuts import render

# Create your views here.
'''
from django.http import HttpResponse
from .models import Category, Course, Student, Instructor
from django.shortcuts import get_object_or_404

def index(request):
    # Fetch categories
    category_list = Category.objects.all().order_by('id')[:10]

    # Fetch up to 5 courses sorted by price in descending order
    course_list = Course.objects.all().order_by('-price')[:5]  # The '-' before 'price' sorts in descending order

    response = HttpResponse()
    heading1 = '<b><p>' + 'List of categories: ' + '</p></b>'
    response.write(heading1)
    for category in category_list:
        para = '<p>'+ str(category) + '</p>'
        response.write(para)

    blank_line = '<br>'
    response.write(blank_line)

    heading2 = '<b><p>' + 'List of courses (sorted by price, descending): ' + '</p></b>'
    response.write(heading2)
    for course in course_list:
        para = '<p>' + str(course.title) + ' - ' + str(course.price) + '</p>'
        response.write(para)

    return response

def about(request):
    return HttpResponse("This is a Distance Education Website! Search our Categories to find all available Courses.")

def detail(request, category_no):
    # Fetch the category using get_object_or_404() which will automatically handle the case if the category does not exist
    category = get_object_or_404(Category, pk=category_no)

    # Fetch courses associated with the category
    courses_for_category = Course.objects.filter(categories=category)

    response = HttpResponse()
    heading = '<h1><p>' + 'Category: ' + str(category.name) + '</p></h1>'
    response.write(heading)

    course_heading = '<b><p>' + 'Courses under this category: ' + '</p></b>'
    response.write(course_heading)
    for course in courses_for_category:
        course_info = '<p>' + str(course.title) + '</p>'
        response.write(course_info)

    return response