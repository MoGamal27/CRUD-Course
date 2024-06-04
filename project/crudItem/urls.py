from django.urls import path
from . import views

urlpatterns = [  
    path('course/', views.getCourse, name='course'),
    path('course/add', views.postCourse, name='course_add'),
     path('course/<int:id>/edit', views.putCourse, name='course_update'),
     path('course/<int:id>', views.getCourseById, name='course_by_id'),
    path('course/<int:id>/delete', views.deleteCourse, name='course_delete'),
   
]