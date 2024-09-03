import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

# dont want to expose all data to algolia for search 
@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        'title',
        'content',
        'price', 
        'user',
        'public'
    ]

    settings = {
        'searchableAttributes': ['title', 'content'],
        'attributesForFaceting': ['user', 'public'] # enables stuff like 'show products by this user', 'show public products'
    }

    tags = 'get_tags_list'