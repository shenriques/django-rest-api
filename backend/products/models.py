from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        # if the search is in the title or the content
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        # only get the products which are public
        query_set = self.is_public().filter(lookup)
        if user is not None:
            # get products only from user that satisfy the search criteria
            query_set_2 = query_set.filter(user=user).filter(lookup)
            # unique items in the combination of query sets
            query_set = (query_set | query_set_2).distinct()
        return query_set

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    # means search() method can run on any queryset
    objects = ProductManager()

    # method to determine if instance gets indexed for algolia
    def is_public(self) -> bool:
        return self.public

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self): # class method
        return "122"
