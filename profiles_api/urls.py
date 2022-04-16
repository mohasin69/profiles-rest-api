from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    #path('hello-view-set/', views.HelloViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('', include(router.urls))
]
