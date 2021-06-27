from django.urls import path, include
from .views import ProductEntryView, ProductExitView
from rest_framework import routers


router = routers.SimpleRouter()
router.register('add_product', ProductEntryView)
router.register('buy_product', ProductExitView)

urlpatterns = [
    path('', include(router.urls))
]
