from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AjyViewSet,
    CategoryPackageViewSet,
    PackageViewSet,
    PhotoPackageViewSet,
    ComboViewSet,
    ArticleOrNewsViewSet,
    LessonViewSet,
)

router = DefaultRouter()
router.register(r'ajy', AjyViewSet, basename='ajy')
router.register(r'category-packages', CategoryPackageViewSet, basename='category-packages')
router.register(r'packages', PackageViewSet, basename='packages')
router.register(r'photo-packages', PhotoPackageViewSet, basename='photo-packages')
router.register(r'combos', ComboViewSet, basename='combos')
router.register(r'articles-or-news', ArticleOrNewsViewSet, basename='articles-or-news')
router.register(r'lessons', LessonViewSet, basename='lessons')


urlpatterns = [
    path('', include(router.urls)),
]
