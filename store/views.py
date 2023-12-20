from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from .forms import QuickAddForm


# def quick_add_product(request):
#     if request.method == 'POST':
#         form = QuickAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product-list')
#     else:
#         form = QuickAddForm(),
#     context = {'form': form}
#     return render(request, 'store/quickadd.html', context)


# Create your views here.

@login_required(login_url='login')
def quick_add_product(request):
    form = QuickAddForm()
    if request.method == 'POST':
        form = QuickAddForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Oluşturan kullanıcıyı atama
            product.save()
            return redirect('product-list')
    context = {'form': form}
    return render(request, 'store/quickadd.html', context)