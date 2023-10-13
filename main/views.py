import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from main.forms import ItemForm
from django.shortcuts import render
from django.urls import reverse
from main.models import item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url='/login')
def show_main(request):
    user = request.user
    context = {
        'name': 'Naufal Mahdy Hanif',
        'class': 'PBP E',
        'appName' : 'AmbatuStore',
        'NPM' : '2206082335',
        'last_login': request.COOKIES['last_login'],
        'username' : user.username,
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_item(request):
    form = ItemForm(request.POST or None)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_items'))
    
    context = {'form': form}
    return render(request, "create_item.html", context)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        image = request.FILES.get('image')

        new_item = item(user=user, name=name, amount=amount, description=description, image = image)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def del_product_ajax(request):
    if request.method == 'POST':
        items = item.objects.filter(user=request.user)
        deletedItem = items.get(pk = request.POST.get('id'))
        deletedItem.delete()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_product_json(request):
    product_item = item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@login_required(login_url='/login')
def show_items(request):
    items = item.objects.filter(user=request.user)
    countItem = items.count()
    if (request.method == 'POST'):
        if 'inc' in request.POST:
            tempPatchedItem = items.get(pk = request.POST.get('inc'))
            patchedItem = items.filter(pk = request.POST.get('inc'))
            newAmount = tempPatchedItem.amount + 1
            patchedItem.update(amount = newAmount)
        elif 'dec' in request.POST:
            tempPatchedItem = items.get(pk = request.POST.get('dec'))
            patchedItem = items.filter(pk = request.POST.get('dec'))
            newAmount = tempPatchedItem.amount -1
            patchedItem.update(amount = newAmount)
        elif 'del' in request.POST:
            deletedItem = items.get(pk = request.POST.get('del'))
            deletedItem.delete()
    context = {
        'username': request.user.username,
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product berdasarkan ID
    items = item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=items)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_items'))

    context = {'form': form}
    return render(request, "edit_item.html", context)