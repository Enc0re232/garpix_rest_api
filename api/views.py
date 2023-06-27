from rest_framework import viewsets
from .serializers import RepositoryInfoSerializers
from restservice.models import RepositoryInfo


class RepositoryInfoViewSets(viewsets.ModelViewSet):
    queryset = RepositoryInfo.objects.all()
    serializer_class = RepositoryInfoSerializers
