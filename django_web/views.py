from django.shortcuts import render
from .models import DjangoWebProductmessage
from django.shortcuts import render
from django.db import connection
from django_web.selectModel import select as se
from django_web.selectModel import word2vec as wv
from django_web.es_search import es_search as es
# Create your views here.
def index(request):
    return  render(request,'index.html')

# first version data transmission
# def search(request):
#     from django_web import models
#     keyword=[]
#     products=[]
#     if 'title' in request.GET and request.GET['title']:
#         get_keyword = request.GET['title']
#         keyword.append(get_keyword)
#         wv.keyword2vec(keyword)
#
#         relativeProducts=se.chu()
#         for i in relativeProducts:
#             products.append(DjangoWebProductmessage.objects.get(id=i))
#     return render(request,'index.html',{'products': products})

# second version data transmission
def search(request):
    from django_web import models
    keyword=""
    products=[]
    if 'title' in request.GET and request.GET['title']:
        get_keyword = request.GET['title']
        print(get_keyword)

        rs=es.search(get_keyword)

        for i in rs['hits']['hits']:
            print(i['_source']['id'])
            product=DjangoWebProductmessage(id=i['_source']['id'],img_url=i['_source']['img_url'],title=i['_source']['title'])
            products.append(product)
    return render(request,'index.html',{'products': products})
