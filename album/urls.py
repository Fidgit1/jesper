from django.urls import path
from album import views

urlpatterns = [
    path("", views.album_index, name="index"),
    path("upload", views.UploadFileView.as_view(), name="upload"),
]
