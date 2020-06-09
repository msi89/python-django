from rest_framework import routers
from examples import views as ex_api
from languages import views as lang_api
from product import views as pdt_api

router = routers.DefaultRouter()
router.register('articles', ex_api.ArticleViewset)
router.register('students', ex_api.StudentViewset)
router.register('courses', ex_api.CourseViewset)
router.register('enrollments', ex_api.EnrollmentViewset)

router.register('languages', lang_api.LanguageViewset)
router.register('paradigms', lang_api.ParadigmViewset)
router.register('programmers', lang_api.ProgrammerViewset)

router.register('categories', pdt_api.CategoryViewset)
router.register('products', pdt_api.ProductViewset)
