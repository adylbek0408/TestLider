from rest_framework import viewsets, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


class AjyViewSet(viewsets.ModelViewSet):
    queryset = Ajy.objects.all()
    serializer_class = AjySerializer


class CategoryPackageViewSet(viewsets.ModelViewSet):
    queryset = CategoryPackage.objects.all()
    serializer_class = CategoryPackageSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'ajy', 'start_tour', 'end_tour']


class PhotoPackageViewSet(viewsets.ModelViewSet):
    queryset = PhotoPackage.objects.all()
    serializer_class = PhotoPackageSerializer


class ComboViewSet(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['combo_choices']

    def list(self, request, *args, **kwargs):
        data = self.request.query_params.get('q', None)
        if data:
            api = Combo.objects.filter(combo_choices=data)
            if api.exists():
                api_serializer = ComboSerializer(api, many=True)
                return Response(api_serializer.data, status=status.HTTP_200_OK)
            else:
                raise NotFound()
        else:
            return super().list(request, *args, **kwargs)


class ArticleOrNewsViewSet(viewsets.ModelViewSet):
    queryset = ArticleOrNews.objects.all()
    serializer_class = ArticleOrNewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['choices']

    def list(self, request, *args, **kwargs):
        data = self.request.query_params.get('q', None)
        if data:
            api = ArticleOrNews.objects.filter(choices=data)
            if api.exists():
                api_serializer = ArticleOrNewsSerializer(api, many=True)
                return Response(api_serializer.data, status=status.HTTP_200_OK)
            else:
                raise NotFound()
        else:
            return super().list(request, *args, **kwargs)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['package', 'date']

