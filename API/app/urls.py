from rest_framework import routers
from .views import AppListViewset, PessoaViewSet

router = routers.DefaultRouter()
router.register(r'lista', AppListViewset)
router.register(r'pessoa', PessoaViewSet)
urlpatterns = router.urls