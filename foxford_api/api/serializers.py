import io

from rest_framework import serializers

from service.models import Teacher, Webinar, Course, TeacherInCourse, TeacherInWebinar


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ('__all__')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('__all__')


class TeacherInCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherInCourse
        fields = ('__all__')


class TeacherInWebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherInWebinar
        fields = ('__all__')
