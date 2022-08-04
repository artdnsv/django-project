from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path('item-add/', views.ItemAdd.as_view(), name="item-add"), 
    path('item-list/', views.ItemList.as_view(),name="item-list"),
    path('item/<int:pk>/', views.ItemView.as_view(),name="item-view"),
    path('item_edit/<int:pk>/', views.ItemEdit.as_view(),name="item-view"),
    path('item_delete /<int:pk>/', views.ItemDelete.as_view(),name="item-delete"),
]