from command.views import CommandViewSet, ArticleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
# Command END POINT
router.register('command', CommandViewSet)
router.register('article', ArticleViewSet)
urlpatterns = router.urls