from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

logger = logging.getLogger(__name__)


def get_all_properties():

    queryset = cache.get("all_properties")
    if not queryset:
        queryset = list(Property.objects.all())
        cache.set("expensive_queryset", queryset, 3600)
    return queryset


def get_redis_cache_metrics():
    redis_connection = get_redis_connection("default")
    info = redis_connection.info("stats")
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)
    total = hits + misses
    total_requests = total
    hit_ratio = hits / total_requests if total_requests > 0 else 0
    logger.error

    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio,
    }
