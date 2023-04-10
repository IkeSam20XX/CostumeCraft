# creating endpoints to view data
from django.http import JsonResponse
from .models import Supply
from .serializers import SupplySerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def supply_list(request):
    if request.method == 'GET':
        #get all the supplies
        supplies = Supply.objects.all()
        #serialize them
        serializer = SupplySerializer(supplies, many=True)
        #return json
        return JsonResponse({'supplies' : serializer.data})
    
    if request.method == 'POST':
        serializer = SupplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

#@api_view(['GET', 'PUT', 'DELETE'])
#def supply_detail(request):

#    if request.method == 'GET':
        
#    elif request.method == 'POST':
#        pass
#    elif request.method == 'DELETE':
#        pass
