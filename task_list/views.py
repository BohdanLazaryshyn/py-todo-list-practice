from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from task_list.form import TagForm, TagSearchForm, TaskSearchForm, TaskForm
from task_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = TaskSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        queryset = queryset.order_by("-done", "-created_datetime")
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            ).distinct()

        return queryset


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list:home")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list:home")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_list:home")


def task_toggle_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse_lazy("task_list:home"))


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 7

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = TagSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Tag.objects.all()
        form = TagSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            ).distinct()

        return queryset


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task_list:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_list:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_list:tag-list")
