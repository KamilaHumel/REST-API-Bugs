from django.urls import path

from .views import BugList, CreateBug, UpdateBug

urlpatterns = [
    path("bugs/", BugList.as_view(), name="get_bugs"),
    path("create/", CreateBug.as_view(), name="create"),
    path("update/<int:pk>/", UpdateBug.as_view(), name="update"),
]
