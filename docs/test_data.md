# SDE test data generation

When developing an application using the SDE data you might want to pre-load a subset of this data for running
your tests.
This documentation explains how to export data in your application for running your unit tests.

## Setup

In your Django application test folder you will create a python module called `testdata`.

This will lead to a structure as follows: `<YOUR-APPLICATION>.tests.testdata`.

In the testdata module you will need to create an `__init__.py` file:

```py
from eve_sde.test_data import ModelSpec

testdata_spec: list[ModelSpec] = [
  ModelSpec(
    "Moon",
    ids=[
      40178441,  # Loads Tama
      40178267,  # Eranakko
      40178195,  # Sujarento
      40178312,  # Onatoh x
      40178362,  # Tannolen
      40178073,  # Nagamanen
      40471667,  # Some wh system
    ],
  ),
  ModelSpec("ItemType", ids=[81143]),  # Magmatic gases
]
```

In this file you need to describe the models you want to export in your tests.
Having a variable `testdata_spec` containing a list of `eve_sde.testdata.ModelSpec` is mandatory.

## Generating the test data

The management command `esde_generate_test_data` will handle all the generation.
You can easily run it using `python manage.py esde_generate_test_data <YOUR-APP-LABEL>`.

Once the command finish running you should fine a new file in your testdata folder called `sde.json`.

## Loading data

To load this data in your django tests you need to add a `fixtures` attribute to your django test classes:

```python
class MyTestCase(TestCase):
    fixtures = ["testdata/sde.json"]
```
