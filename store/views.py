from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from .forms import QuickAddForm


def quick_add_product(request):
    if request.method == 'POST':
        form = QuickAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')  
    else:
        form = QuickAddForm()
    return render(request, 'templates/store/quickadd.html', {'form': form})


# Create your views here.


"""def addProduct(request):
    if request.method == "POST":
        form = QuickProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("")

    else:
        form = QuickProductForm()
    return render(request, 'index.html', {'form': form})"""


@login_required(login_url='login')
def QuickAdd(request):
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