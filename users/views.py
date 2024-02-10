from django.shortcuts import render
def about_me(request):
    return render(request, 'users/about_me.html')
# Create your views here.
