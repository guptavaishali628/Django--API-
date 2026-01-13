from django.shortcuts import render
from django.http import HttpResponse
from .models import movie
import json
from django.forms import model_to_dict  # model data convert into dictionary
from django.views.decorators.csrf import csrf_exempt  # to ignore the error of csrf token when the post method hit by third party apllication


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

@csrf_exempt
def movie_detail(req,pk):

#----------------------------------------------------PUT-------------------------------------------------------------  
    if req.method=='PUT':
        j_data=req.body  #thunder client se a rha hai data for updation
        # print(j_data)
        # print(type(j_data))

        # converts json data into python new data:
        newPy_data=json.loads(j_data)  # python new data:
        # print(newPy_data) 
        # print(type(newPy_data))

        old_data=movie.objects.get(id=pk) # python old data:
        # oldpy_data=model_to_dict(old_data)  # convert models data into python data isko hum jab use krenge jab hum old_data ki key ko dictionary ka use krenge lekin usse hum save ni kr skte hai
        
        #------------------validations---------------------
        if newPy_data.get('name', False) and newPy_data.get('dis', False) and newPy_data.get('active', False):
            old_data.name=newPy_data['name']
            old_data.dis=newPy_data['dis']
            old_data.active=newPy_data['active']
            old_data.save()
        
            d={'msg':'object updated successfully'}
            jd=json.dumps(d)
        
            return HttpResponse(jd, content_type='application/json')
        
        else:
            d={'msg':'some fields are missing'}
            jd=json.dumps(d)
        
            return HttpResponse(jd, content_type='application/json')

#------------------------------------------------------------PATCH------------------------------------------------------
    
    elif req.method=='PATCH':
        j_data=req.body  #thunder client se a rha hai data for partially updation
        # print(j_data)
        # print(type(j_data))

        # converts json data into python new data:
        newPy_data=json.loads(j_data)  # python new data:
        # print(newPy_data) 
        # print(type(newPy_data))

        old_data=movie.objects.get(id=pk) # python old data:
        # oldpy_data=model_to_dict(old_data)  # convert models data into python data
        
        #------------------validations---------------------
        if newPy_data.get('name', False): 
            old_data.name=newPy_data['name']
        if newPy_data.get('dis', False):
            old_data.dis=newPy_data['dis']
        if newPy_data.get('active', False):
            old_data.active=newPy_data['active']
        old_data.save()
        
        d={'msg':'object partially updated successfully'}
        jd=json.dumps(d)
    
        return HttpResponse(jd, content_type='application/json')
        

    elif req.method=='DELETE':
        if req.method=='DELETE':
            id=movie.objects.filter(id=pk)
            if id:
                data=movie.objects.get(id=pk)
                data.delete()

                p_data={'msg': 'object deleted'}
                j_data=json.dumps(p_data)
                return HttpResponse(j_data, content_type='application/json')
        p_data= {'msg':'id not found'}
        j_data= json.dumps(p_data)
        return HttpResponse(j_data, content_type='application/json')    

    data=movie.objects.get(id=pk)
    # print(data)
    # print(type(data))

    #converting models data into python dictionary:'
    p_data=model_to_dict(data)
    print(p_data)
    print(type(p_data))

    # convert p_data to json data:
    j_data=json.dumps(p_data)
    # print(j_data)
    # print(type(j_data))
    return HttpResponse(j_data, content_type='application/json')

