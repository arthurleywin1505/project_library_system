from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('books/', include('books.urls')),
    path('members/', include('members.urls')),
    path('reservations/', include('reservations.urls')),
    ]