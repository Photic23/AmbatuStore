from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import item
from django.http import HttpResponse
from django.core import serializers



def show_main(request):
    context = {
        'name': 'Naufal Mahdy Hanif',
        'class': 'PBP E',
        'appName' : 'AmbatuStore',
        'NPM' : '2206082335',
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_items'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_items(request):
    items = item.objects.all()
    countItem = item.objects.all().count()
    context = {
        'items' : items,
        'itemCount' : countItem
    }
    return render(request, "item.html", context)

def show_xml(request):
    data = item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


