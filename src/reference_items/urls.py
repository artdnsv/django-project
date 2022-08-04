from django.urls import path
from . import views

app_name = "ref"

urlpatterns = [
    #Genre
    path('genre_add/', views.GenreAdd.as_view(), name="genre-add"),
    path('genre_list/', views.GenreList.as_view(), name="genre-list"),
    path('genre/<int:pk>/', views.GenreView.as_view(), name="genre-view"),
    path('genre_edit/<int:pk>', views.GenreEdit.as_view(), name="genre-edit"),
    path('genre_delete/<int:pk>', views.GenreDelete.as_view(), name="genre-delete"),
    #Author
    path('author_add/', views.AuthorAdd.as_view(), name="author-add"),
    path('author_list/', views.AuthorList.as_view(), name="author-list"),
    path('author/<int:pk>/', views.AuthorView.as_view(), name="author-view"),
    path('author_edit/<int:pk>', views.AuthorEdit.as_view(), name="author-edit"),
    path('author_delete/<int:pk>', views.AuthorDelete.as_view(), name="author-delete"),
    #Publisher
    path('publisher_add/', views.PublishereAdd.as_view(), name="publisher-add"),
    path('publisher_list/', views.PublisherList.as_view(), name="publisher-list"),
    path('publisher/<int:id>/', views.PublisherView.as_view(), name="publisher-view"),
    path('publisher_edit/<int:pk>', views.PublisherEdit.as_view(), name="publisher-edit"),
    path('publisher_delete/<int:pk>', views.PublisherDelete.as_view(), name="publisher-delete"),
    #Series
    path('series_add/', views.SeriesAdd.as_view(), name="publisher-add"),
    path('series_list/', views.SeriesList.as_view(), name="publisher-list"),
    path('series/<int:pk>/', views.SeriesView.as_view(), name="publisher-view"),
    path('series_edit/<int:pk>', views.SeriesEdit.as_view(), name="publisher-edit"),
    path('series_delete/<int:pk>', views.SeriesDelete.as_view(), name="gepublishernre-delete") 
]