from django.core.cache import cache
from .models import Property


def getallproperties():
    queryset = cache.get("all_properties")
    if not queryset:
        queryset = Property.objects.all()
        cache.set("expensive_queryset", queryset, 3600)
    return queryset
