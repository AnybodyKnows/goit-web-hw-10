from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .utils import get_mongodb
from .forms import AuthorAddForm, QuoteAddForm
from .models import Author, Quotes
from django.contrib.auth.decorators import login_required


def main(request, page=1):
    quotes = Quotes.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)

    return render(request, 'quot/index.html', context={'quotes': quotes_on_page})


@login_required(login_url='/auth/signin/')
def add_author(request):

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quot:root')
        else:
            return render(request, 'quot/add_author.html', {'form': form})

    return render(request, 'quot/add_author.html', {'form': AuthorAddForm()})


@login_required(login_url='/auth/signin/')
def add_quote(request):
    if request.method == 'POST':
        form = QuoteAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quot:root')  # Redirect to the main page after successful form submission
        else:
            return render(request, 'quot/add_quote.html', {'form': form})

    form = QuoteAddForm()
    return render(request, 'quot/add_quote.html', {'form': form})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quot/author_detail.html', {'author': author})
