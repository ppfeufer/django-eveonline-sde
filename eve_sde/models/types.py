"""
    Eve type models
"""
# Django
from django.db import models
from django.db.models import Model

# AA Example App
from eve_sde.models.utils import get_langs_for_field, lang_key


class TypeBase(Model):
    id = models.BigIntegerField(
        primary_key=True
    )

    name = models.CharField(
        max_length=250
    )

    class Meta:
        abstract = True
        default_permissions = ()

    def __str__(self):
        return f"{self.name} ({self.id})"


class ItemCategory(TypeBase):
    """
    categories.jsonl
        _key : int
        name : dict
            name.de : str
            name.en : str
            name.es : str
            name.fr : str
            name.ja : str
            name.ko : str
            name.ru : str
            name.zh : str
        published : bool
        iconID : int
    """
    # JsonL Params
    _filename = "categories.jsonl"
    _update_fields = [
        "name",
        "published",
        "iconID",
        *get_langs_for_field("name"),
    ]

    # Model Fields
    published = models.BooleanField(default=False)
    iconID = models.IntegerField(null=True, blank=True, default=None)

    @classmethod
    def from_jsonl(cls, json_data, names=False):
        cat = cls(
            id=json_data.get("_key"),
            name=json_data.get("name")["en"],
            published=json_data.get("published"),
            iconID=json_data.get("iconID"),
        )

        for lang, name in json_data.get("name", {}).items():
            setattr(cat, f"name_{lang_key(lang)}", name)

        return cat


class ItemGroup(TypeBase):
    """
    groups.jsonl
        _key : int
        anchorable : bool
        anchored : bool
        categoryID : int
        fittableNonSingleton : bool
        name : dict
            name.de : str
            name.en : str
            name.es : str
            name.fr : str
            name.ja : str
            name.ko : str
            name.ru : str
            name.zh : str
        published : bool
        useBasePrice : bool
        iconID : int
    """
    # JsonL Params
    _filename = "categories.jsonl"
    _update_fields = [
        "name",
        "published",
        "iconID",
        *get_langs_for_field("name"),
    ]

    # Model Fields
    published = models.BooleanField(default=False)
    iconID = models.IntegerField(null=True, blank=True, default=None)

    @classmethod
    def from_jsonl(cls, json_data, names=False):
        cat = cls(
            id=json_data.get("_key"),
            name=json_data.get("name")["en"],
            published=json_data.get("published"),
            iconID=json_data.get("iconID"),
        )

        for lang, name in json_data.get("name", {}).items():
            setattr(cat, f"name_{lang_key(lang)}", name)

        return cat


class ItemType(TypeBase):
    """
    types.jsonl
        _key : int
        groupID : int
        mass : float
        name : dict
            name.de : str
            name.en : str
            name.es : str
            name.fr : str
            name.ja : str
            name.ko : str
            name.ru : str
            name.zh : str
        portionSize : int
        published : bool
        volume : float
        radius : float
        description : dict
            description.de : str
            description.en : str
            description.es : str
            description.fr : str
            description.ja : str
            description.ko : str
            description.ru : str
            description.zh : str
        graphicID : int
        soundID : int
        iconID : int
        raceID : int
        basePrice : float
        marketGroupID : int
        capacity : float
        metaGroupID : int
        variationParentTypeID : int
        factionID : int

    """
    pass


class DogmaAttribute(TypeBase):
    """
    dogmaAttributes.jsonl
        _key : int
        attributeCategoryID : int
        dataType : int
        defaultValue : float
        description : str
        displayWhenZero : bool
        highIsGood : bool
        name : str
        published : bool
        stackable : bool
        displayName : dict
            displayName.de : str
            displayName.en : str
            displayName.es : str
            displayName.fr : str
            displayName.ja : str
            displayName.ko : str
            displayName.ru : str
            displayName.zh : str
        iconID : int
        tooltipDescription : dict
            tooltipDescription.de : str
            tooltipDescription.en : str
            tooltipDescription.es : str
            tooltipDescription.fr : str
            tooltipDescription.ja : str
            tooltipDescription.ko : str
            tooltipDescription.ru : str
            tooltipDescription.zh : str
        tooltipTitle : dict
            tooltipTitle.de : str
            tooltipTitle.en : str
            tooltipTitle.es : str
            tooltipTitle.fr : str
            tooltipTitle.ja : str
            tooltipTitle.ko : str
            tooltipTitle.ru : str
            tooltipTitle.zh : str
        unitID : int
        chargeRechargeTimeID : int
        maxAttributeID : int
    """
    pass


class DogmaAttribute(TypeBase):
    """
    typeDogma.jsonl
        _key : int
        dogmaAttributes : list
        dogmaEffects : list
    """
    pass


class Dogma(TypeBase):
    """
    typeDogma.jsonl
        _key : int
        dogmaAttributes : list
        dogmaEffects : list
    """
    pass


class DogmaAttributeCategory(TypeBase):
    """
    dogmaAttributeCategories.jsonl
        _key : int
        description : str
        name : str
    """
    pass


class DogmaUnit(TypeBase):
    """
    dogmaUnits.jsonl
        _key : int
        description : dict
            description.de : str
            description.en : str
            description.es : str
            description.fr : str
            description.ja : str
            description.ko : str
            description.ru : str
            description.zh : str
        displayName : dict
            displayName.de : str
            displayName.en : str
            displayName.es : str
            displayName.fr : str
            displayName.ja : str
            displayName.ko : str
            displayName.ru : str
            displayName.zh : str
        name : str
    """
    pass


class DogmaEffect(TypeBase):
    """
    dogmaEffects.jsonl
        _key : int
        disallowAutoRepeat : bool
        dischargeAttributeID : int
        durationAttributeID : int
        effectCategoryID : int
        electronicChance : bool
        guid : str
        isAssistance : bool
        isOffensive : bool
        isWarpSafe : bool
        name : str
        propulsionChance : bool
        published : bool
        rangeChance : bool
        distribution : int
        falloffAttributeID : int
        rangeAttributeID : int
        trackingSpeedAttributeID : int
        description : dict
            description.de : str
            description.en : str
            description.es : str
            description.fr : str
            description.ja : str
            description.ko : str
            description.ru : str
            description.zh : str
        displayName : dict
            displayName.de : str
            displayName.en : str
            displayName.es : str
            displayName.fr : str
            displayName.ja : str
            displayName.ko : str
            displayName.ru : str
            displayName.zh : str
        iconID : int
        modifierInfo : list
        npcUsageChanceAttributeID : int
        npcActivationChanceAttributeID : int
        fittingUsageChanceAttributeID : int
        resistanceAttributeID : int
    """
    pass


class typeMaterials(TypeBase):
    """
    typeMaterials.jsonl
        _key : int
        materials : list
        randomizedMaterials : list
    """
