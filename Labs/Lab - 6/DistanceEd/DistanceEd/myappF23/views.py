from django.http import HttpResponse
from .models import Category, Course, Student, Instructor
from django.shortcuts import get_object_or_404
from django.shortcuts import render

def index(request):
    # Fetch categories
    category_list = Category.objects.all().order_by('id')[:10]

    # Fetch up to 5 courses sorted by price in descending order
    course_list = Course.objects.all().order_by('-price')[:5]  # The '-' before 'price' sorts in descending order

    response = HttpResponse()
    heading1 = '<p><b>'  + 'List of categories: ' + '</p></b>'
    response.write(heading1)
    for category in category_list:
        para = '<p>'+ str(category) + '</p>'
        response.write(para)

    heading2 = '<p><b>' + 'List of courses (sorted by price, descending): ' + '</p></b>'
    response.write(heading2)
    for course in course_list:
        para = '<p>' + str(course.title) + ' - ' + str(course.price) + '</p>'
        response.write(para)

    return render(request, 'index0.html', {'category_list': category_list})
    #return response

def about(request):
    #return HttpResponse("This is a Distance Education Website! Search our Categories to find all available Courses.")
    return render(request, 'about0.html')
"""
#old detail view
def detail(request, category_no):
    # Fetch courses associated with the category
    courses_for_category = Course.objects.filter(categories=category)

    response = HttpResponse()
    heading = '<p>' + 'Category: ' + str(category.name) + '</p>'
    response.write(heading)

    course_heading = '<p>' + 'Courses under this category: ' + '</p>'
    response.write(course_heading)
    for course in courses_for_category:
        course_info = '<p>' + str(course.title) + '</p>'
        response.write(course_info)
    return response
"""
#lab 6 detail view TEMPLATES FOR CATEGORY_DETAIL0
def detail(request, category_no):
    category = get_object_or_404(Category, pk=category_no)
    courses_for_category = Course.objects.filter(categories=category)
    context = {
        'category': category,
        'courses_for_category': courses_for_category
    }
    return render(request, 'category_detail0.html', context)

"""

4.c Do you need to pass any extra context variables to the template?
4.d If yes, what variable(s) are you passing?
None (since we're not passing any extra context variables to the template).

Explanation:
The about0.html template simply displays static content and provides links to the main page. It doesn't require any dynamic data from the database or any other source, so no context variables are needed.
def detail(request, category_no):
    # Fetch the category using get_object_or_404() which will automatically handle the case if the category does not exist
    category = get_object_or_404(Category, pk=category_no)
    
    
5c. Do you need to pass any extra context variables to the template?
YES
5d. If yes, what variable(s) are you passing?
The variables being passed are:
category: An instance of the selected category based on the provided ID (category_no).
courses_for_category: A list of courses that are associated with the selected category.

"""

def instructor_courses(request, instructor_id):
    # Fetch the instructor by ID
    instructor = get_object_or_404(Instructor, pk=instructor_id)

    # Since the students are related to the instructor through the Course model,
    # we first need to fetch courses taught by the instructor.
    courses_taught = Course.objects.filter(instructor=instructor)

    # Now, fetch students who took the courses taught by the instructor
    students = Student.objects.filter(course__in=courses_taught).distinct()

    context = {
        'instructor': instructor,
        'students': students
    }

    return render(request, 'instructor_detail.html', context)

