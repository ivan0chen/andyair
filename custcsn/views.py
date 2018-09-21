from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from custcsn.models import Custcsn
from custcsn.forms import CustcsnForm


@login_required
def custcsnList(request, template_name='custcsn/custcsnList.html'):
    custcsns = Custcsn.objects.all()
    ctx = {}
    ctx['custcsns'] = custcsns
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def custcnsCreate(request, template_name='custcsn/custcsnForm.html'):
    form = CustcsnForm(request.POST or None)
    if form.is_valid():
        new_cust = form.save(commit=False)
        new_cust.created_by = request.user
        new_cust.last_updated_by = request.user
        new_cust.save()
        messages.success(request, '資料已新增！')
        # return redirect('custcsn:custcsnUpdate', new_cust.id)
        return redirect('custcsn:custcsnList')
    ctx = {}
    ctx['form'] = form
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

@login_required
def custcsnView(request, pk, template_name='custcsn/custcsnView.html'):
    custcsn = get_object_or_404(Custcsn, pk=pk)
    form = CustcsnForm(instance=custcsn)
    ctx = {}
    ctx['custcsn'] = custcsn
    ctx['form'] = form
    ctx['title'] = 'View'
    return render(request, template_name, ctx)

@login_required
def custcsnUpdate(request, pk, template_name='custcsn/custcsnForm.html'):
    custcsn = get_object_or_404(Custcsn, pk=pk)
    form = CustcsnForm(request.POST or None, instance=custcsn)
    if form.is_valid():
        cuscsn_obj = form.save(commit=False)
        cuscsn_obj.last_updated_by = request.user
        cuscsn_obj.save()
        messages.success(request, '資料已更新！')
        # return redirect('custcsn:custcsnUpdate', custcsn.id)
        return redirect('custcsn:custcsnList')
    ctx = {}
    ctx['custcsn'] = custcsn
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

@login_required
def custcsnDelete(request, pk, template_name='custcsn/custcsnDelete.html'):
    custcsn = get_object_or_404(Custcsn, pk=pk)
    form = CustcsnForm(instance=custcsn)
    if request.method == 'POST':
        custcsn.delete()
        messages.success(request, '資料已刪除！')
        return redirect('custcsn:custcsnList')
    ctx = {}
    ctx['custcsn'] = custcsn
    ctx['form'] = form
    ctx['title'] = 'Delete'
    return render(request, template_name, ctx)