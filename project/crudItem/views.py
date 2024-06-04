from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.views import View
from .models import Course
import json

# Create your views here.
def getCourse(request):
        courses = list(Course.objects.values())
        return JsonResponse(courses, safe=False)

@csrf_exempt
def postCourse(request):
     if request.method == 'POST':
      data = json.loads(request.body)
      course = Course.objects.create(name=data['name'], price=data['price'])
     return JsonResponse({'id': course.id, 'name': course.name, 'price': course.price}, status=201)

def putCourse(request, id):
            try:
               course = Course.objects.get(id=id)
               if request.method == 'PUT':
                  data = json.loads(request.body)
                  course.name = data['name']
                  course.price = data['price']
                  course.save()
                  return JsonResponse({'id': course.id, 'name': course.name, 'price': course.price})
            except Course.DoesNotExist:
               return JsonResponse({'error': 'Course not found'}, status=404)
            
def getCourseById(request, id):
            try:
               course = Course.objects.get(id=id)
               return JsonResponse({'id': course.id, 'name': course.name, 'price': course.price})
            except Course.DoesNotExist:
               return JsonResponse({'error': 'Course not found'}, status=404)

def deleteCourse(request, id):
            try:
               course = Course.objects.get(id=id)
               if request.method == 'DELETE':
                  course.delete()
                  return JsonResponse ({'result': 'Course deleted'}, status=204)
            except Course.DoesNotExist:
                   return JsonResponse({'error': 'Course not found'}, status=404)                        
              
           


