import json
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from product.models import Product

def api_home(request, *args, **kwargs):
    database_data= Product.objects.all().order_by("?").first()
    data ={}
    if database_data:
        data['name']=database_data.name
        data['identity']=database_data.id
        data['price']=database_data.price
        data['description']=database_data.description


    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body) # Strings of Json data --> python String
    # except:
    #     pass

    # # print(data.keys())
    # print(data)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    return JsonResponse(data)