from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewset)
router.register(r'workplans', views.WorkplanViewset)
router.register(r'milestones', views.MileStoneViewset)
router.register(r'supplys', views.SupplyViewset)
router.register(r'travels', views.TravelViewset)