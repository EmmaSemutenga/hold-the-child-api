from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'programs', views.ProgramViewset)
router.register(r'programmatic_approaches', views.ProgrammaticApproachViewset)
router.register(r'indicators', views.IndicatorViewset)
router.register(r'management_approaches', views.ManagementApproachViewset)
router.register(r'milestones', views.MileStoneViewset)