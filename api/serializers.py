from rest_framework import serializers
from restservice.models import RepositoryInfo


class RepositoryInfoSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    branches = serializers.JSONField(default=list)
    tags = serializers.JSONField(default=list)

    class Meta:
        fields = ('name', 'branches', 'tags')
        model = RepositoryInfo
