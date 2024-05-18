from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from shop.forms import CourseForm, UploadFileForm
from shop.models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})


def auth(request):
    return render(request, 'shop/auth.html')


def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()

    return render(request, 'shop/add_course.html', {'title': 'Add Course', 'form': form})


# class add_course(CreateView):
#     form_class = CourseForm
#     template_name = 'shop/add_course.html'
#     extra_context = {'title': 'Add Course'}
#     success_url = reverse_lazy()


class add_course(View):
    def get(self, request):
        form = CourseForm()
        return render(request, 'shop/add_course.html', {'title': 'Add Course', 'form': form})

    def post(self, request):
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'shop/add_course.html', {'title': 'Add Course', 'form': form})
