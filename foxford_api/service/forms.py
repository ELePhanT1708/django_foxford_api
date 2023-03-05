from django import forms

from .models import Teacher, Course, Level, Webinar, StatusWebinar


class AddTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'last_name']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control",
                                           "placeholder": "Иван"}),
            'surname': forms.TextInput(attrs={"class": "form-control",
                                              "placeholder": "Павлович"}),
            'last_name': forms.TextInput(attrs={"class": "form-control",
                                                "placeholder": "Смирнов"}),
        }


class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'duration_in_days', 'level', 'price']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control",
                                           "placeholder": "Геометрия для 9 классов"}),
            'duration_in_days': forms.NumberInput(),
            'level': forms.Select(choices=Level.choices,),
            'price': forms.NumberInput(),
        }


class AddWebinar(forms.ModelForm):
    class Meta:
        model = Webinar
        fields = ['planned_time', 'name', 'status', 'duration_in_hours', 'course_id', 'teachers']
        widgets = {
            'planned_time': forms.DateTimeInput(),
            'name': forms.NumberInput(),
            'status': forms.Select(choices=StatusWebinar.choices,),
            'duration_in_hours': forms.NumberInput(),
            'course_id': forms.Select(),
            'teachers': forms.Select(),
        }