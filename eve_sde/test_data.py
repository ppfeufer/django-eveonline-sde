# Standard Library
from dataclasses import dataclass

# Django
from django.apps import apps
from django.core import serializers

# AA Example App
from eve_sde.models import JSONModel


@dataclass
class ModelSpec:
    """Defines a model to be saved in a file for testing"""
    model_name: str
    ids: list[int]


def dump_model_data(specs: list[ModelSpec]) -> str:
    """
    Saves the given model specs into a file for reuse
    """

    objects_to_dump = []

    for spec in specs:

        model = _get_model_class(spec)

        objects_to_dump.extend(model.objects.filter(id__in=spec.ids))

    serialized_data = serializers.serialize("json", objects_to_dump)

    return serialized_data


def _get_model_class(spec: ModelSpec) -> type[JSONModel]:
    """Returns the class associated with a spec"""

    model = apps.get_model("eve_sde", spec.model_name)

    if not issubclass(model, JSONModel):
        raise TypeError(f"Invalid model class {spec.model_name}")

    return model
