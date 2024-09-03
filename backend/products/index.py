import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

# dont want to expose all data to algolia for search 
@register(Product)
class ProductIndex(AlgoliaIndex):
    # filter the instances that get indexed (public must be True  )
    should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price', 
        'user',
        'public'
    ]