from django.shortcuts import render


def main(request):
    return render(request, 'quot/index.html', context={})
