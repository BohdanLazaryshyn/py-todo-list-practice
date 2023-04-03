from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_list.form import TagForm, TagSearchForm
from task_list.models import Task, Tag


class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('done', '-created_datetime')


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag

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


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task_list:tag-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task_list:tag-list")
