from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet, PostsList, PostDetails

router = routers.DefaultRouter()
router.register('user',UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('posts/',PostsList.as_view(),name='posts'),
    path('<int:pk>/',PostDetails.as_view(),name='post_details'),
]