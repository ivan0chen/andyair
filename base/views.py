from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from base.models import Custadv, Custqtn
from base.forms import CustadvForm, CustqtnForm

@login_required
def custadvList(request, template_name='base/custadvList.html'):
    custadvs = Custadv.objects.all()
    ctx = {}
    ctx['custadvs'] = custadvs
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def custadvCreate(request, template_name='base/custadvForm.html'):
    form = CustadvForm(request.POST or None)
    if form.is_valid():
        new_cust = form.save(commit=False)
        new_cust.created_by = request.user
        new_cust.last_updated_by = request.user
        new_cust.save()
        messages.success(request, '資料已新增！')
        return redirect('base:custadvUpdate', new_cust.id)
    ctx = {}
    ctx['form'] = form
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

@login_required
def custadvView(request, pk, template_name='base/custadvView.html'):
    custadv = get_object_or_404(Custadv, pk=pk)
    ctx = {}
    ctx['custadv'] = custadv
    ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
    ctx['title'] = 'View'
    return render(request, template_name, ctx)

@login_required
def custadvUpdate(request, pk, template_name='base/custadvForm.html'):
    custadv = get_object_or_404(Custadv, pk=pk)
    form = CustadvForm(request.POST or None, instance=custadv)
    if form.is_valid():
        custadv_obj = form.save(commit=False)
        custadv_obj.last_updated_by = request.user
        custadv_obj.save()
        messages.success(request, '資料已更新！')
        return redirect('base:custadvUpdate', custadv.id)
    ctx = {}
    ctx['custadv'] = custadv
    ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

@login_required
def custadvDelete(request, pk, template_name='base/custadvDelete.html'):
    custadv = get_object_or_404(Custadv, pk=pk)
    if request.method == 'POST':
        custadv.delete()
        messages.success(request, '資料已刪除！')
        return redirect('base:custadvList')
    ctx = {}
    ctx['custadv'] = custadv
    ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
    ctx['title'] = 'Delete'
    return render(request, template_name, ctx)

@login_required
def custadvData(request, pk):
    custadv = get_object_or_404(Custadv, pk=pk)
    ctx = {}
    if request.POST.get('requestData') == 'master':
        ctx['custadv'] = custadv
        template_name = 'base/custMaster.html'
    else:
        ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
        template_name = 'base/custDetail.html'
    return render(request, template_name, ctx)

@login_required
def custqtnNew(request, parent_pk, template_name='base/custqtnNew.html'):
    custadv = get_object_or_404(Custadv, pk=parent_pk)
    form = CustqtnForm(request.POST or None)
    if form.is_valid():
        custqtn = form.save(commit=False)
        custqtn.custadv = custadv
        custqtn.created_by = request.user
        custqtn.last_updated_by = request.user
        custqtn.save()
        messages.success(request, '明細資料已新增！')
        return redirect('base:custadvUpdate', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["custadv"] = custadv
    ctx['custqtns'] = Custqtn.objects.filter(custadv=custadv)
    ctx['title'] = ' New Detail'
    return render(request, template_name, ctx)

@login_required
def custqtnTabledit(request):
    if request.method == 'POST':
        custqtn = get_object_or_404(Custqtn, pk=request.POST.get('id'))
        if request.POST.get('action') == 'edit':
            custqtn.org = request.POST.get('org')
            custqtn.qtndd = datetime.strptime(request.POST.get('qtndd'),"%Y-%m-%d").date()
            custqtn.qtns = request.POST.get('qtns')
            custqtn.last_updated_by = request.user
            custqtn.save()
            messages.success(request, '明細資料已更新！')
        if request.POST.get('action') == 'delete':
            custqtn.delete()
            messages.success(request, '明細資料已刪除！')

        django_messages = []
        for message in messages.get_messages(request):
            django_messages.append({
                "level": message.level,
                "message": message.message,
                "tags": message.tags,
            })
        ctx = {}
        ctx['request'] = request.POST
        ctx['messages'] = django_messages

        return JsonResponse(ctx)
        # return JsonResponse(request.POST)
    else:
        return render(request, 'main/main.html')


