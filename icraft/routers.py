from rest_framework import routers
from timesheet.viewsets import EntryViewSet

router = routers.DefaultRouter()

router.register(r'timesheet', EntryViewSet)