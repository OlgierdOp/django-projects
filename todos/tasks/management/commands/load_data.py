
from django.core.management.base import BaseCommand, CommandError
from tasks.services import TaskLoadData
from tasks.models import Todo


class Command(BaseCommand):
    help = 'ładuje dane'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        tld = TaskLoadData(klass=Todo)
        tld.insert()
        print("Done")

