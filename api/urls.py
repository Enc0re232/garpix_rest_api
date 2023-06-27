from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RepositoryInfoViewSets

app_name = 'api'

router_1 = DefaultRouter()
router_1.register('repos', RepositoryInfoViewSets)

urlpatterns = [
    path('', include(router_1.urls)),
]
