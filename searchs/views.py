from django.shortcuts import render


# Create your views here.
def search_list(request):
    return render(request, 'search/search.html')
