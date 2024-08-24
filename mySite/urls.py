from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('plantas.urls')),
    path('api-auth/', include('rest_framework.urls')),  
    path('api/', include('plantas.urls')),  
] 
