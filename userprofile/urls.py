from rest_framework.routers import DefaultRouter

from chat.views import *
from userprofile.views import UserViewSet,ContactAndLinksViewSet

router=DefaultRouter()
router.register('user',UserViewSet,basename='user')
router.register('contacts_and_links',ContactAndLinksViewSet,basename='contacts_and_links')
urlpatterns = router.urls