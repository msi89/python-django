from django.contrib import admin
from .models import Article, Student, Course, Enrollment

admin.site.register(Article)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
