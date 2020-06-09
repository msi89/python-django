from django.db import models

# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    student = models.ManyToManyField(Student, through='Enrollment')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
    final_grade = models.CharField(max_length=1, blank=True, null=True)

    # class Meta:
    #     unique_together = [['student', 'course']]
