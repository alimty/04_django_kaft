from django.urls import path, include
from django.contrib import admin
from page.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('manage/', include('page.urls'),),
    path('user/', include('user_profile.urls'), ),
    path('', index, name="index"),
]
