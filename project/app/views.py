from django.shortcuts import render
from django.http import HttpResponse
from .models import movie
import json
# to ignore the error of csrf token when the post method hit by third party apllication
from django.views.decorators.csrf import csrf_exempt


# Create your views here
# decorator.
@csrf_exempt
def movie_list(req):
    if req.method=='POST':
        j_data=req.body   #this data is in json format
        print(j_data) 
        p_data=json.loads(j_data)   # convert it into python data
        print(p_data)
        print(type(p_data))

        # we are sending multiple data object in form of list of dictionary so we have to use for loop:
        for i in p_data:
            n=i['name']
            d=i['dis']
            # a=i['active']
            a=i.get('active',True)  # when we send active bydefault true:
            movie.objects.create(name=n, dis=d, active=a)

        # creating data in databas:
        # movie.objects.create(name=p_data['name'], dis=p_data['dis'], active=p_data['active'])
        dic={'msg': 'object created successfully...'}
        j_d=json.dumps(dic)
        return HttpResponse(j_d,content_type='application/json')
    else:
        
        # for get which take bydefault
        data= movie.objects.all()    
    
        # jsn_data=json.dumps(data)
        # print(jsn_data)  # give error of serializers because this data from database is not a python data 
    
        # print(data)
        # print(data.values())
        # print(list(data.values())) # data convert into python

        data=list(data.values()) # tycasting data into python list data
        jsn_data=json.dumps(data)  # convert python data into json data
        # print(jsn_data)

        return HttpResponse(jsn_data, content_type='application/json')


def movie_detail(req):
    pass
