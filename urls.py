from django.urls import path, include 


urlpatterns = [
  path('', include('sw_admin.api.urls')),
]
