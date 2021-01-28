from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'donors', views.DonorViewSet)
router.register(r'vendors', views.VendorViewSet)