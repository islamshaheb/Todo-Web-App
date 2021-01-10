from django.shortcuts import render,redirect
from .models import list
from .forms import listform
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = listform(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = list.objects.all
            messages.success(request,'Your item has been added to the list')
            return render(request,"index.html",{'all_items':all_items})

    else:
        all_items = list.objects.all
        return render(request,"index.html",{'all_items':all_items})


def delete(request,list_id):
    item = list.objects.get(pk = list_id)
    item.delete()
    messages.success(request,('Item has been deleted successfully'))
    return redirect('ba')

def cut(request,list_id):
    item = list.objects.get(pk=list_id)
    item.complete = True
    item.save()
    return redirect('ba')

def uncut(request, list_id):
    item = list.objects.get(pk=list_id)
    item.complete =  False
    item.save()
    return redirect('ba')

def edit(request,list_id):
    if request.method == 'POST':
        item = list.objects.get(pk=list_id)
        form = listform(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,('Item has been Edited'))
            return redirect('ba')
    else:
        item = list.objects.get(pk=list_id)
        return render(request,'edit.html',{'item':item})





















