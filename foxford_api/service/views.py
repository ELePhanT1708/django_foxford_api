from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView

from .forms import AddCourse, AddTeacher, AddWebinar
from .models import Course, Webinar, Teacher


# Create your views here.
def add_course(request):
    if request.method == "POST":
        form = AddCourse(request.POST)
        if form.is_valid():
            course = Course(name=form.cleaned_data.get('name'),
                            duration_in_days=form.cleaned_data.get('duration_in_days'),
                            level=form.cleaned_data.get('level'),
                            price=form.cleaned_data.get('price'),
                            )
            course.save()
            messages.success(request, 'Course was created ! ')
            return redirect('home')
    else:
        form = AddCourse()
    return render(request, 'service/add_course.html', {'form': form,
                                                       'title': 'Добавить курс'})


def add_webinar(request):
    if request.method == "POST":
        form = AddWebinar(request.POST)
        if form.is_valid():
            webinar = Course(name=form.cleaned_data.get('name'),
                             surname=form.cleaned_data.get('surname'),
                             last_name=form.cleaned_data.get('last_name'),
                             )
            webinar.save()
            messages.success(request, 'Teacher was added ! ')
            return redirect('home')
    else:
        form = AddWebinar()
    return render(request, 'service/add_webinar.html', {'form': form,
                                                        'title': 'Добавить вебинар'})


def add_teacher(request):
    if request.method == "POST":
        form = AddTeacher(request.POST)
        if form.is_valid():
            teacher = Course(name=form.cleaned_data.get('name'),
                             surname=form.cleaned_data.get('surname'),
                             last_name=form.cleaned_data.get('last_name'),
                             )
            teacher.save()
            messages.success(request, 'Teacher was added ! ')
            return redirect('home')
    else:
        form = AddTeacher()
    return render(request, 'service/add_teacher.html', {'form': form,
                                                        'title': 'Добавить преподавателя'})


class ViewHome(ListView):
    model = Course
    template_name = 'service/home_page.html'


class ViewWebinars(ListView):
    model = Webinar
    context_object_name = 'webinars'
    template_name = 'service/view_webinars.html'
    extra_context = {'title': 'FOXFORD PLATFORM'}
    paginate_by = 3

    def get_queryset(self):
        return Webinar.objects.all()


class ViewTeachers(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'service/view_teachers.html'
    extra_context = {'title': 'FOXFORD PLATFORM'}
    paginate_by = 3

    def get_queryset(self):
        return Teacher.objects.all()


class ViewCourses(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'service/view_courses.html'
    extra_context = {'title': 'FOXFORD PLATFORM'}
    paginate_by = 3

    def get_queryset(self):
        return Course.objects.all()
