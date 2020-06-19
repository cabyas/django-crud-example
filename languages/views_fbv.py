from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from languages.models import Language
from languages.forms import CreateLanguageForm


def home_view(request):
    languages = Language.objects.all()
    paginator = Paginator(languages, 10)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        raise Http404(f'Invalid page {page_number}. That page contains no results')

    context = {
        'object_list': page_obj,
        'page_obj': page_obj
    }
    return render(request, 'languages/index.html', context)


def language_details_view(request, pk):
    language = get_object_or_404(Language, pk=pk)
    context = {
        'language': language
    }
    return render(request, 'languages/language_detail.html', context)


def language_create_view(request):
    if request.method == 'POST':
        form = CreateLanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            return redirect(language.get_absolute_url())
    else:
        form = CreateLanguageForm()

    return render(request, 'languages/language_create.html', {'form': form})


def language_update_view(request, pk):
    if request.method == 'POST':
        form = CreateLanguageForm(request.POST)
        if form.is_valid():
            language = form.save()
            return redirect(language.get_absolute_url())
    else:
        language = get_object_or_404(Language, pk=pk)
        form = CreateLanguageForm(instance=language)

    context = {
        'edit': True,
        'form': form
    }
    return render(request, 'languages/language_create.html', context)


def language_delete_view(request, pk):
    language = get_object_or_404(Language, pk=pk)
    if request.method == 'POST':
        language.delete()
        return redirect(reverse('languages:home'))
        
    context = {
        'language': language
    }
    return render(request, 'languages/confirm_language_deletion.html', context)
    