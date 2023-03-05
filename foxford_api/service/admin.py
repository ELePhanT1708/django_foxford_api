from django.contrib import admin
from .models import (Webinar, Teacher, Course,
                     TeacherInCourse, TeacherInWebinar)


# Register your models here.
admin.site.register(Webinar)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(TeacherInCourse)
admin.site.register(TeacherInWebinar)