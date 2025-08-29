from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property
from django.http import JsonResponse


@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all()

    return JsonResponse({"data": property})
