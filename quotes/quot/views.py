from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .utils import get_mongodb
from .forms import AuthorAddForm


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)

    return render(request, 'quot/index.html', context={'quotes': quotes_on_page})


def add_author(request):

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quot:root')
        else:
            return render(request, 'quot/add_author.html', {'form': form})

    return render(request, 'quot/add_author.html', {'form': AuthorAddForm()})
