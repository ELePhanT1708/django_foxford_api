from rest_framework import viewsets

from service.models import Webinar, Course, Teacher, TeacherInWebinar, TeacherInCourse
from .serializers import WebinarSerializer, TeacherSerializer, CourseSerializer, TeacherInWebinarSerializer, \
    TeacherInCourseSerializer


# Create your views here.


class WebinarModelViewSet(viewsets.ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer


class CourseModelViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherInWebinarModelViewSet(viewsets.ModelViewSet):
    queryset = TeacherInWebinar.objects.all()
    serializer_class = TeacherInWebinarSerializer


class TeacherInCourseModelViewSet(viewsets.ModelViewSet):
    queryset = TeacherInCourse.objects.all()
    serializer_class = TeacherInCourseSerializer

