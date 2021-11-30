from django.urls import path
from landing.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'), # class-based views need to have '.as_view' after the view name. Index is set as root file.

]