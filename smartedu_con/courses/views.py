from multiprocessing import context
from django.shortcuts import render
from .models import Courses

# Create your views here.

def course_list(request):
    courses= Courses.objects.all().order_by("-date")

    context= {
        "courses":courses
    }

    return render(request, "courses.html", context)


def course_detail(request, category_slug, course_id):
    course= Courses.objects.get()