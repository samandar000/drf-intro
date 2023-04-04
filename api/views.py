from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response



@api_view(['GET','POST'])
def hi(request: Request) -> Response:
    '''hi view'''
    if request.method == 'GET':
        params = request.query_params
        
        name = params.get('name', '')
        print(type(name))

        return Response(f'hi, {name}')
    elif request.method == 'POST':
        params = request.data
        name = params.get('name','')

@api_view(['GET'])
def addition(request: Request) -> Response:
    '''add two number'''
    if request.method == 'GET':
        params = request.query_params

        a = params.get('a',0)
        b = params.get('b',0)
        c = int(a)+int(b)

        return Response({'answer':c})
    elif request.method  == 'POST':
        a = params.get('a',0)
        b = params.get('b',0)
        c = int(a)+int(b)

    

@api_view(['GET'])
def subtract(request: Request) -> Response:
    '''add two number'''
    params = request.query_params

    a = params.get('a',0)
    b = params.get('b',0)
    c = int(a)-int(b)

    return Response({'answer':c})




@api_view(['GET'])
def multiply(request: Request) -> Response:
    '''add two number'''
    params = request.query_params

    a = params.get('a',0)
    b = params.get('b',0)
    c = int(a)*int(b)

    return Response({'answer':c})



@api_view(['GET'])
def devide(request: Request) -> Response:
    '''add two number'''
    params = request.query_params

    a = params.get('a',0)
    b = params.get('b',0)
    b = int(b)
    
    
    if b != 0:
        c = int(a)/int(b)
    else:
        c = int(a)

    return Response({'answer':c})
