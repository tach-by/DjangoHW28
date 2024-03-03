from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.api.views import (
    UserViewSet,
    ProductsApiView,
    category_list,
    ArticleGenericAPIView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductsApiView.as_view()),
    path('categories/', category_list),
    path('articles/<int:pk>/', ArticleGenericAPIView.as_view())
]