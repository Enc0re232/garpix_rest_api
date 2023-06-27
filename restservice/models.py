from django.db import models
from django.conf import settings


class RepositoryInfo(models.Model):
    name = models.CharField(
        max_length=settings.NAME_MAX_LENGTH
    )
    branches = models.JSONField(default=list)
    tags = models.JSONField(default=list)

    class Meta:
        verbose_name = 'Репозиторий'
        verbose_name_plural = 'Репозитории'

    def __str__(self):
        return self.name
