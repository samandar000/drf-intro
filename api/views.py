from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def hi(request: Request) -> Response:
    '''hi view'''
    params = request.query_params
    
    name = params.get('name', '')

    print(f'hi, {name}')