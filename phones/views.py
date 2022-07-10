from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    if sort == 'name':
        phone_object = Phone.objects.order_by('name')
        context = {'phones': phone_object}
        return render(request, template, context)
    if sort == 'min_price':
        phone_object = Phone.objects.order_by('price')
        context = {'phones': phone_object}
        return render(request, template, context)
    if sort == 'max_price':
        phone_object = Phone.objects.order_by('-price')
        context = {'phones': phone_object}
        return render(request, template, context)
    else:
        phone_object = Phone.objects.all()
        context = {'phones': phone_object}
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    context = {'phone': phone_object[0]}
    return render(request, template, context)
