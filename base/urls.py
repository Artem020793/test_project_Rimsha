from django.contrib import admin
from django.urls import path, include
from api.models import ProductResource, LessonResource
from tastypie.api import Api

api = Api(api_name='v1')
lesson_recource = LessonResource()
product_recource = ProductResource()
api.register(lesson_recource)
api.register(product_recource)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('api/', include(api.urls))
]
