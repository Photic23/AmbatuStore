from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Naufal Mahdy Hanif',
        'class': 'PBP E',
        'appName' : 'AmbatuStore',
        'NPM' : '2206082335',
    }

    return render(request, "main.html", context)

def show_items(request):
    context = {
        'name' : 'Ambatupen',
        'amount' : '3',
        'description' : 'A pen used by the infamouse Mr. Rusdi'
    }

    return render(request, "item.html", context)
