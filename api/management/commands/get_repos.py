import json

from django.core.management.base import BaseCommand

from api.utils import get_all_repos, get_branch_and_tags
from restservice.models import RepositoryInfo


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        repos_list = get_all_repos('JenIK-s', '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')

        for i, repo in enumerate(repos_list):
            repos = get_branch_and_tags('JenIK-s', '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', repo)
            name, branches, tags = repos[0], repos[1], repos[2]


            RepositoryInfo.objects.create(
                name=name,
                branches=branches,
                tags=tags
            )
            print(f'{i + 1}/{len(repos_list)}')
