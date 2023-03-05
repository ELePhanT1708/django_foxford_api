from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Course(models.Model):
    class Level(models.TextChoices):
        STUDENTS = 'ST', _('Students')
        PUPILS = 'PP', _('Pupils')
        TEACHERS = 'TH', _('Teachers')

    name = models.CharField(max_length=100, verbose_name="Название курса")
    duration_in_days = models.IntegerField(verbose_name='Длительность курса в днях')
    level = models.CharField(max_length=20,
                             choices=Level.choices,
                             default=Level.STUDENTS)
    price = models.FloatField(verbose_name='Цена курса в рублях')


class Teacher(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя преподавателя')
    surname = models.CharField(max_length=40, verbose_name='Отчество преподавателя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия преподавателя')
    courses = models.ManyToManyField(Course, related_name='teachers', through='TeacherInCourse',
                                     through_fields=('teacher', 'course'))


class Webinar(models.Model):
    class StatusWebinar(models.TextChoices):
        CREATED = 'CR', _('Created')
        CANCELLED = 'CN', _('Cancelled')
        NOW = 'NW', _('Now')
        FINISHED = 'FI', _('Finished')

    planned_time = models.DateTimeField(verbose_name='Планируемое время начало вебинара', )
    name = models.CharField(max_length=50, verbose_name='Название вебинара')
    status = models.CharField(max_length=10,
                              choices=StatusWebinar.choices,
                              default=StatusWebinar.CREATED,
                              verbose_name='Статус вебинара')
    duration_in_hours = models.IntegerField(verbose_name='Продолжительность вебинара в часах')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    teachers = models.ManyToManyField(Teacher, related_name='webinars',
                                      through='TeacherInWebinar',
                                      through_fields=('webinar', 'teacher'))


class TeacherInCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    salary_for_hour = models.FloatField(verbose_name='Цена за час в курсе')


class TeacherInWebinar(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE)
