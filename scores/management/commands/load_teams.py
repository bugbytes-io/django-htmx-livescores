from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load EPL teams and fixtures'

    def handle(self, *args, **kwargs):
        raise NotImplementedError