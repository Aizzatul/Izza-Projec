from django.contrib import admin
from django.urls import path
from xaxa import views
urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.xaxa,name='xaxa'),
]