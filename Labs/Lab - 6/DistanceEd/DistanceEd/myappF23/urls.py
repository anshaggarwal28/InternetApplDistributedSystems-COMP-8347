from django.urls import path
from myappF23 import views

app_name = 'myappF23'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # URL pattern for the about view
    path('<int:category_no>/', views.detail, name='detail'),  # URL pattern for the detail view using named groups
    path('index0/', views.index, name='index0'),
    path('about0/', views.about, name='about0'),  # URL pattern for the about0 view
    path('<int:category_no>/', views.detail, name='detail'), #category_detail0 view templates lab6
    path('instructor/<int:instructor_id>/', views.instructor_courses, name='instructor_detail'),

]
