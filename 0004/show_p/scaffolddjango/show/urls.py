from rest_framework.routers import DefaultRouter

from django.conf.urls import url, include
from .views import *


router = DefaultRouter()
router.register('brand', BrandViewSet)
router.register('item', ItemViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
