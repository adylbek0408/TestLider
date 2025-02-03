from rest_framework import serializers
from .models import Ajy, CategoryPackage, Package, PhotoPackage, Combo, ArticleOrNews, Lesson


class AjySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ajy
        fields = ['id', 'name', 'bio', 'image']


class CategoryPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPackage
        fields = ['id', 'name']


class PhotoPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoPackage
        fields = ['id', 'package', 'image']


class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['id', 'name', 'rich', 'image', 'date', 'package', 'combo_choices']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'package', 'date', 'video_url', 'description']


class PackageSerializer(serializers.ModelSerializer):
    package_categories = CategoryPackageSerializer(read_only=True)
    package_ajy = AjySerializer(read_only=True)
    photo_packages = PhotoPackageSerializer(many=True, read_only=True)
    packages = ComboSerializer(many=True, read_only=True)
    lesson_packages = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = [
            'id', 'package_categories', 'package_ajy', 'name', 'description', 'start_tour', 'end_tour',
            'photo_packages', 'packages', 'lesson_packages']


class ArticleOrNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleOrNews
        fields = ['id', 'name', 'description', 'image', 'date', 'choices']
