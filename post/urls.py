from post.views import boasts, post_message, roasts, top_posts
from django.urls import include, path
from post import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post-list', views.PostViewSet)

urlpatterns = [
    path('posts/<int:id>/', views.vote),
    path('posts/boast/', views.boasts),
    path('posts/roast/', views.roasts),
    path('posts/top/', views.top_posts),
    path('posts/post/', views.post_message),
    path('posts/', include(router.urls)),
]
