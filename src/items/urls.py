from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('item_add/', views.ItemAdd.as_view(), name="item-add"), 
    path('item_list/', views.ItemList.as_view(),name="item-list"),
    path('item/<int:pk>/', views.ItemView.as_view(),name="item-view"),
    path('item_edit/<int:pk>/', views.ItemEdit.as_view(),name="item-edit"),
    path('item_delete/<int:pk>/', views.ItemDelete.as_view(),name="item-delete"),
] 