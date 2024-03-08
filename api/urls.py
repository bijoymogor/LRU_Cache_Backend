from django.urls import path
from .views import LRUCacheAPI


urlpatterns = [
    path('get/<str:key>/', LRUCacheAPI.as_view()),
    path('set/', LRUCacheAPI.as_view())
]
