from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm,StoreCreateForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def store_create(request):
	# if request.user.is_anonymous:
	# 	return redirect('signin')
	form = StoreCreateForm()
	if request.method == "POST":
		form = StoreCreateForm(request.POST,)
		if form.is_valid():
			store.save()
			return redirect('store-list')
	context = {
		"form": form,
	}
	return render(request, 'create.html', context)

def store_detail(request, store_slug):
	store = Store.objects.get(slug=store_slug)
	context = {
		"store": store,
		"slug" : store_slug,
	}
	return render(request, 'detail.html', context)

