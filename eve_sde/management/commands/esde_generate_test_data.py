# Standard Library
from importlib import import_module

# Django
from django.core.management.base import BaseCommand

# AA Example App
from eve_sde.test_data import dump_model_data


class Command(BaseCommand):
    help = "Generates test data for an application."

    def add_arguments(self, parser):
        parser.add_argument("module", type=str)

    def handle(self, *args, **options):
        module_name = options["module"]
        module = import_module(module_name)

        spec = module.testdata_spec

        dumped_data = dump_model_data(spec)

        with open("test.json", "w") as f:
            f.write(dumped_data)
