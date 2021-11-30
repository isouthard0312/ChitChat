from django.shortcuts import render
from django.views import View

class Index(View): #allows user to make different methods for each HTTP request.
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')

        
