from django.urls import path
from myappF23 import views

app_name = 'myappF23'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # URL pattern for the about view
    path('<int:category_no>/', views.detail, name='detail'),  # URL pattern for the detail view using named groups
]

