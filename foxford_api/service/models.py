from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Level(models.TextChoices):
    STUDENTS = 'ST', _('Students')
    PUPILS = 'PP', _('Pupils')
    TEACHERS = 'TH', _('Teachers')


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса")
    duration_in_days = models.IntegerField(verbose_name='Длительность курса в днях')
    level = models.CharField(max_length=20,
                             choices=Level.choices,
                             default=Level.STUDENTS)
    price = models.FloatField(verbose_name='Цена курса в рублях')

    def __str__(self):
        return f'< Курс: {self.name} >'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Teacher(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя преподавателя')
    surname = models.CharField(max_length=40, verbose_name='Отчество преподавателя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия преподавателя')
    courses = models.ManyToManyField(Course, related_name='teachers', through='TeacherInCourse',
                                     through_fields=('teacher', 'course'))

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'< Преподаватель: {self.name} {self.surname} {self.last_name} >'


class StatusWebinar(models.TextChoices):
    CREATED = 'CR', _('Created')
    CANCELLED = 'CN', _('Cancelled')
    NOW = 'NW', _('Now')
    FINISHED = 'FI', _('Finished')


class Webinar(models.Model):


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

    class Meta:
        verbose_name = 'Вебинар'
        verbose_name_plural = 'Вебинары'

    def __str__(self):
        return f'< Вебинар: {self.name} >'


class TeacherInCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    salary_for_hour = models.FloatField(verbose_name='Цена за час в курсе')

    class Meta:
        verbose_name = 'Преподаватель в курсе'
        verbose_name_plural = 'Преподаватели в курсах'

    def __str__(self):
        return f'<{self.teacher.__str__()} в {self.course.__str__()} >'


class TeacherInWebinar(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE)

    def __str__(self):
        return f'<{self.teacher.__str__()} в {self.webinar.__str__()} >'

    class Meta:
        verbose_name = 'Преподаватель в вебинаре'
        verbose_name_plural = 'Преподаватели в вебинарах'
