from django.shortcuts import render


def home(request):
    data = {
        'title': 'Общество "Fsociety"'
    }
    return render(request, 'main/home.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')