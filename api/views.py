from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .lru_cache import LRUCache

# Create your views here.

cache = LRUCache(1024)

class LRUCacheAPI(APIView):
    def get(self, request, key):
        value = cache.get(key)
        return Response({'key': key, 'value': value})
    
    def post(self,request):
        key = request.data.get('key')
        value = request.data.get('value')
        expiration = int(request.data.get('expiration', 5))  # Default expiration: 5 seconds
        cache.set(key, value, expiration)
        return Response({'message': 'Value set successfully'})




