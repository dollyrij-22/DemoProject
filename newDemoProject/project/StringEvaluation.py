from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

@api_view(['POST'])
def stringEvaluation(request):
    try:
        #get input
        input = JSONParser().parse(request)

        #evaluate input
        number = eval(input['expression'])

        #return response
        return HttpResponse(number, status=200)
    except Exception as e:
        print('Exception % s' % e)