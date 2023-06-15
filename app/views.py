from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@permission_classes([IsAuthenticated])
class ProductCrud(APIView):
    def get(self, request, id):
        PQS = Product.objects.all()
        PJD = ProductSerializer(PQS, many=True)
        return Response(PJD.data)
    
    def post(self, request, id):
        PMSD = ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PSO = PMSD.save()
            return Response({'success':'Product is created'})
        else:
            return Response({'Failed':'Product is not created'})
        
    def put(self, request, id):
        id = request.data['id']
        productobject = Product.objects.get(id=id)
        PMSD = ProductSerializer(productobject,data=request.data)
        if PMSD.is_valid():
            PSO = PMSD.save()
            return Response({'success':'Product is updated'})
        else:
            return Response({'Failed':'Product is not updated'})
        
    def patch(self, request, id):
        id = request.data['id']
        productobject = Product.objects.get(id=id)
        PMSD = ProductSerializer(productobject,data=request.data, partial=True)
        if PMSD.is_valid():
            PSO = PMSD.save()
            return Response({'success':'Product is partially updated'})
        else:
            return Response({'Failed':'Product is not updated'})
    
    def delete(self, request, id):
        Product.objects.get(id=id).delete()
        return Response({'success':'Product is Deleted'})