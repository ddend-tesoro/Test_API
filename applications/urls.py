from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('applicatons', views.ApplicationView)

urlpatterns = [
    # path('', views.test_api, name='index'),
    path('', include(router.urls))

]
