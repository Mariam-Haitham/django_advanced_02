from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def detail (request, store_slug):
	slug = Store.objects.get(slug = store_slug)
	context = {
		"slug": slug,
	}
	return render(request, "detail.html", context)

def create(request):

	form = StoreModelForm()
	if request.method == "POST":
		form = StoreModelForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('list')
		print (form.errors)
	context = {
		"form": form,
	}
	return render(request, 'create.html', context)


