from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='sistem')
def dashboard(request):
    return render(request, "dashboard.html")
