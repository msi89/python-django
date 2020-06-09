from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from . import serializers, models


class ArticleViewset(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.AllowAny]


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    # authentication_classes = (TokenAuthentication, )


class CourseViewset(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class EnrollmentViewset(viewsets.ModelViewSet):
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer
