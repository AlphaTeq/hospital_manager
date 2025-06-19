from django.apps import apps

for model in apps.get_models():
    print(f"\nModel: {model.__name__}")
    for field in model._meta.fields:
        print(f"  - {field.name}: {field.get_internal_type()}")