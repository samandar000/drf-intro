from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def hi(request: Request) -> Response:
    '''hi view'''
    print(request.query_params)
    print('\n'*5)