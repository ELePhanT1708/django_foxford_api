from django.urls import path, include
from rest_framework import routers

from .views import WebinarModelViewSet, TeacherModelViewSet, CourseModelViewSet, TeacherInWebinarModelViewSet, \
    TeacherInCourseModelViewSet

router = routers.DefaultRouter()
router.register(r'webinar', WebinarModelViewSet)
router.register(r'course', CourseModelViewSet)
router.register(r'teacher', TeacherModelViewSet)
router.register(r'teacher_in_webinar', TeacherInWebinarModelViewSet)
router.register(r'teacher_in_course', TeacherInCourseModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]