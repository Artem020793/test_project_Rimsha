from tastypie.resources import ModelResource
from product.models import Product, Lesson
from .authentication import CustomAuthentication
from tastypie.authentication import Authentication


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        allowed_methods = ['get']


class LessonResource(ModelResource):
    class Meta:
        queryset = Lesson.objects.all()
        recource_name = 'lessons'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authentication()
