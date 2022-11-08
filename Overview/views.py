from django.shortcuts import render
from django.views import View

class Overview(View):
    def get(seldf, request):
        return render(request, 'Overview/Overview_Interface.html')