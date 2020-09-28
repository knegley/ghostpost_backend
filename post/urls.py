from django.urls import include, path
from post import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post-list', views.PostViewSet)

urlpatterns = [
    path('posts/', include(router.urls)),
]
