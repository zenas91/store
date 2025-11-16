from django.forms import DecimalField
from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.db.models import Value, F, ExpressionWrapper
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from store.models import Product, Order, OrderItem, Customer, Collection, Cart, CartItem
from tags.models import TaggedItem
from .tasks import notify_customers
import requests


# Transaction is used to ensure everything is successful, otherwise any successful operation will be rolled back
# @transaction.atomic()
# @cache_page(5 * 10)
# def say_hello(request):
# c_queryset = Order.objects.select_related(
#    'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
# qs = OrderItem.objects.values('product__id').distinct()
# queryset = Product.objects.filter(
#    id__in=qs).order_by('title').values('id', 'title')

# return render(request, 'hello.html', {'name': 'Zeus', 'products': list(queryset)})

# result = Product.objects.filter(
#    collection__id=3).aggregate(count=Count('id'), min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price'))

# queryset = Customer.objects.annotate(
#     total_spent=Sum(F('order__orderitem__unit_price') * F('order__orderitem__quantity')))

# ew = ExpressionWrapper(F('order__orderitem__unit_price') * F('order__orderitem__quantity'),
#                       output_field=DecimalField())
# queryset = Product.objects.annotate(
#    quantity_sold=Sum(F('orderitem__quantity'))).annotate(total_sales=Sum(F('orderitem__unit_price') * F('orderitem__quantity'))).order_by('-quantity_sold')[:5]

# with transaction.atomic(): # This can be used when only part of the code is to be wrapped in a transaction using context manager
# queryset = TaggedItem.objects.get_tags_for(Product, 1)

# return render(request, 'hello.html', {'name': 'Zeus', 'result': list(queryset)})

# notify_customers.delay('Hello')
# response = requests.get('https://httpbin.org/delay/2')
# data = response.json()

# return render(request, 'hello.html', {'name': data})


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()

        return render(request, 'hello.html', {'name': data})
