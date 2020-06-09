from django.urls import path, include
from rest_framework import routers
from languages import views

router = routers.DefaultRouter()
router.register('languages', views.LanguageViewset)
router.register('paradigms', views.ParadigmViewset)
router.register('programmers', views.ProgrammerViewset)

urlpatterns = [
    path('', include(router.urls))
]
