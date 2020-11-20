from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>",views.entry, name='entry page'),
    path("search/",views.search,name='search'),
    path("newpage/", views.newPage, name='newPage'),
    path('edit/<str:entry>', views.edit, name='edit'),
    path("random/", views.randompg, name='random')
]
