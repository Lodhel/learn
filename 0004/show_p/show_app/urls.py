from rest_framework.routers import DefaultRouter

from django.conf.urls import url, include
from . import views


router = DefaultRouter()
router.register('brand', views.BrandViewSet)
router.register('item', views.ItemViewSet)
router.register('order', views.OrderViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]