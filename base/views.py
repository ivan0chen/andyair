from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from datetime import datetime
from base.models import Custadv, Custqtn
from base.forms import CustadvForm, CustqtnForm


def custadvList(request, template_name='base/custadvList.html'):
    custadvs = Custadv.objects.all()
    ctx = {}
    ctx['custadvs'] = custadvs
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

def custadvCreate(request, template_name='base/custadvForm.html'):
    form = CustadvForm(request.POST or None)
    if form.is_valid():
        new_cust = form.save(commit=True)
        return redirect('base:custadvUpdate', new_cust.id)
    ctx = {}
    ctx['form'] = form
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

def custadvView(request, pk, template_name='base/custadvView.html'):
    custadv = get_object_or_404(Custadv, pk=pk)
    ctx = {}
    ctx['custadv'] = custadv
    ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
    ctx['title'] = 'View'
    return render(request, template_name, ctx)

def custadvUpdate(request, pk, template_name='base/custadvForm.html'):
    custadv = get_object_or_404(Custadv, pk=pk)
    form = CustadvForm(request.POST or None, instance=custadv)
    if form.is_valid():
        form.save()
        return redirect('base:custadvUpdate', custadv.id)
    ctx = {}
    ctx['custadv'] = custadv
    ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

def custadvDelete(request, pk, template_name='base/custadvDelete.html'):
    custadv = get_object_or_404(Custadv, pk=pk)
    if request.method == 'POST':
        custadv.delete()
        return redirect('base:custadvList')
    ctx = {}
    ctx['custadv'] = custadv
    ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
    ctx['title'] = 'Delete'
    return render(request, template_name, ctx)

def custqtnNew(request, parent_pk, template_name='base/custqtnNew.html'):
    custadv = get_object_or_404(Custadv, pk=parent_pk)
    form = CustqtnForm(request.POST or None)
    if form.is_valid():
        custqtn = form.save(commit=False)
        custqtn.custadv = custadv
        custqtn.save()
        return redirect('base:custadvUpdate', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["custadv"] = custadv
    ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
    ctx['title'] = ' New Detail'
    return render(request, template_name, ctx)

# def custqtnCreate(request, parent_pk, template_name='base/custqtnForm.html'):
#     custadv = get_object_or_404(Custadv, pk=parent_pk)
#     form = CustqtnForm(request.POST or None)
#     if form.is_valid():
#         custqtn = form.save(commit=False)
#         custqtn.custadv = custadv
#         custqtn.save()
#         return redirect('base:custadvView', parent_pk)
#     ctx = {}
#     ctx["form"] = form
#     ctx["custadv"] = custadv
#     ctx['title'] = ' New Detail'
#     return render(request, template_name, ctx)
#
# def custqtnUpdate(request, pk, template_name='base/custqtnForm.html'):
#     custqtn = get_object_or_404(Custqtn, pk=pk)
#     parent_pk = custqtn.custadv.pk
#     form = CustqtnForm(request.POST or None, instance=custqtn)
#     if form.is_valid():
#         form.save()
#         return redirect('base:custadvView', parent_pk)
#     ctx={}
#     ctx['form'] = form
#     ctx['custadv'] = custqtn.custadv
#     ctx['title'] = ' Edit Detail'
#     return render(request, template_name, ctx)
#
# def custqtnDelete(request, pk, template_name='base/custqtnDelete.html'):
#     custqtn = get_object_or_404(Custqtn, pk=pk)
#     parent_pk = custqtn.custadv.pk
#     if request.method == 'POST':
#         custqtn.delete()
#         return redirect('base:custadvView', parent_pk)
#     ctx = {}
#     ctx['custqtn'] = custqtn
#     ctx['custadv'] = custqtn.custadv
#     ctx['title'] = ' Delete Detail'
#     return render(request, template_name, ctx)

def custqtnTabledit(request):
    if request.method == 'POST':
        custqtn = get_object_or_404(Custqtn, pk=request.POST.get('id'))
        if request.POST.get('action') == 'edit':
            custqtn.org = request.POST.get('org')
            custqtn.qtndd = datetime.strptime(request.POST.get('qtndd'),"%Y-%m-%d").date()
            custqtn.qtns = request.POST.get('qtns')
            custqtn.last_update_date = datetime.now()
            custqtn.last_updated_by = 1
            custqtn.save()
        if request.POST.get('action') == 'delete':
            custqtn.delete()
        return JsonResponse(request.POST)
    else:
        return render(request, 'main/main.html')


