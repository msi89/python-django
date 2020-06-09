from rest_framework import viewsets, permissions
from .models import Language, Paradigm, Programmer
from .serializers import (
    LanguageSerializer, ParadigmSerializer, ProgrammerSerializer)

# Create your views here.


class LanguageViewset(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ParadigmViewset(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerViewset(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
