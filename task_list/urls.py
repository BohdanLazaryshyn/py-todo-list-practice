from django.urls import path

from task_list.views import TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskListView

urlpatterns = [
    path("", TaskListView.as_view, name="home"),
    path(
        "tags",
        TagListView.as_view(),
        name="tag-list",
    ), path(
        "tagcreate/",
        TagCreateView.as_view(),
        name="tag-create"
    ), path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ), path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    )
]

app_name = "task_list"
