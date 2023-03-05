# Generated by Django 4.1.7 on 2023-03-05 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название курса')),
                ('duration_in_days', models.IntegerField(verbose_name='Длительность курса в днях')),
                ('level', models.CharField(choices=[('ST', 'Students'), ('PP', 'Pupils'), ('TH', 'Teachers')], default='ST', max_length=20)),
                ('price', models.FloatField(verbose_name='Цена курса в рублях')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Имя преподавателя')),
                ('surname', models.CharField(max_length=40, verbose_name='Отчество преподавателя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия преподавателя')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInWebinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_time', models.DateTimeField(verbose_name='Планируемое время начало вебинара')),
                ('name', models.CharField(max_length=50, verbose_name='Название вебинара')),
                ('status', models.CharField(choices=[('CR', 'Created'), ('CN', 'Cancelled'), ('NW', 'Now'), ('FI', 'Finished')], default='CR', max_length=10, verbose_name='Статус вебинара')),
                ('duration_in_hours', models.IntegerField(verbose_name='Продолжительность вебинара в часах')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.course')),
                ('teachers', models.ManyToManyField(related_name='webinars', through='service.TeacherInWebinar', to='service.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='teacherinwebinar',
            name='webinar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.webinar'),
        ),
        migrations.CreateModel(
            name='TeacherInCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_for_hour', models.FloatField(verbose_name='Цена за час в курсе')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(related_name='teachers', through='service.TeacherInCourse', to='service.course'),
        ),
    ]
