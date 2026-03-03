# Standard Library
from dataclasses import dataclass

# Django
from django.apps import apps
from django.core import serializers
from django.db.models import Model

# AA Example App
from eve_sde.models import JSONModel


def return_all_parent_model_fields(model: type[Model]) -> list[type[Model]]:
    """Returns all parent models of a given model recursively"""
    parents = set()
    for f in model._meta.fields:
        if f.is_relation and f.related_model:
            _f = getattr(model, f.name, None)
            if _f:
                parents.add(_f)
                parents.update(return_all_parent_model_fields(_f))
    return list(parents)


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
    parent_models = []
    for spec in specs:

        model = _get_model_class(spec)
        qry = model.objects.filter(id__in=spec.ids)
        for mdl in qry:
            parent_models += return_all_parent_model_fields(mdl)

        parent_models.reverse()
        objects_to_dump.extend(parent_models)
        objects_to_dump.extend(qry)

    serialized_data = serializers.serialize("json", objects_to_dump)

    return serialized_data


def _get_model_class(spec: ModelSpec) -> type[JSONModel]:
    """Returns the class associated with a spec"""

    model = apps.get_model("eve_sde", spec.model_name)

    if not issubclass(model, JSONModel):
        raise TypeError(f"Invalid model class {spec.model_name}")

    return model
