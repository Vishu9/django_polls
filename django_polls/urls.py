
from django.contrib import admin
from django.urls import path, include
import polls.views
from django.views import generic

urlpatterns = [


    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]