from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from languages.models import Language


class HomeView(ListView):
    model = Language
    template_name = 'languages/index.html'
    paginate_by = 10


class LanguageDetailView(DetailView):
    model = Language
    template_name = 'languages/language_detail.html'


class LanguageCreateView(CreateView):
    model = Language
    template_name = 'languages/language_create.html'
    fields = ['name', 'compiled', 'learned_at', 'main_paradigm', 'observations']


class LanguageUpdateView(UpdateView):
    model = Language
    template_name = 'languages/language_create.html'
    fields = ['name', 'compiled', 'learned_at', 'main_paradigm', 'observations']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class LanguageDeleteView(DeleteView):
    model = Language
    success_url = reverse_lazy('languages:home')
    template_name = 'languages/confirm_language_deletion.html'