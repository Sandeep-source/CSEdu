from .models import Student, Enrollment, Certificate

from django.forms import ModelForm
from student.models import Contact
from franchise.models import Franchise

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__' 
        exclude = ["id","status"]
    def __init__(self, user, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        if user.is_superuser:
           self.fields['institute'].queryset = Franchise.objects.all()
        else:
           self.fields['institute'].queryset = Franchise.objects.filter(id=user.last_name)


class EnrollmentForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'
        exclude = ["id"]
    def __init__(self, *args, **kwargs):
            super(EnrollmentForm, self).__init__(*args, **kwargs)
            self.fields['student_id'].queryset = Student.objects.filter(status='APPROVED')

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        exclude = ['src']
    def __init__(self, *args, **kwargs):
        super(CertificateForm, self).__init__(*args, **kwargs)
        self.fields['Student_id'].queryset = Student.objects.filter(status='APPROVED')

class ContactForm(ModelForm):
     class Meta:
          model = Contact
          exclude = ["id","resolved"]
        