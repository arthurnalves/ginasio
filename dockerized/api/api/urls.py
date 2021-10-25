from django.contrib import admin
from django.urls import path, include

import logic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logic/', include('logic.urls')),
]
