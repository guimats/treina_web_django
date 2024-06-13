from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from todos.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
