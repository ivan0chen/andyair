from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shpr.models import Shpr
from shpr.forms import ShprForm


@login_required
def shprList(request, template_name='shpr/shprList.html'):
    shprs = Shpr.objects.all()
    ctx = {}
    ctx['shprs'] = shprs
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def shprCreate(request, template_name='shpr/shprForm.html'):
    form = ShprForm(request.POST or None)
    if form.is_valid():
        new_cust = form.save(commit=False)
        new_cust.created_by = request.user
        new_cust.last_updated_by = request.user
        new_cust.save()
        messages.success(request, '資料已新增！')
        # return redirect('shpr:shprUpdate', new_cust.id)
        return redirect('shpr:shprList')
    ctx = {}
    ctx['form'] = form
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

@login_required
def shprView(request, pk, template_name='shpr/shprView.html'):
    shpr = get_object_or_404(Shpr, pk=pk)
    form = ShprForm(instance=shpr)
    ctx = {}
    ctx['shpr'] = shpr
    ctx['form'] = form
    ctx['title'] = 'View'
    return render(request, template_name, ctx)

@login_required
def shprUpdate(request, pk, template_name='shpr/shprForm.html'):
    shpr = get_object_or_404(Shpr, pk=pk)
    form = ShprForm(request.POST or None, instance=shpr)
    if form.is_valid():
        cuscsn_obj = form.save(commit=False)
        cuscsn_obj.last_updated_by = request.user
        cuscsn_obj.save()
        messages.success(request, '資料已更新！')
        # return redirect('shpr:shprUpdate', shpr.id)
        return redirect('shpr:shprList')
    ctx = {}
    ctx['shpr'] = shpr
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

@login_required
def shprDelete(request, pk, template_name='shpr/shprDelete.html'):
    shpr = get_object_or_404(Shpr, pk=pk)
    form = ShprForm(instance=shpr)
    if request.method == 'POST':
        shpr.delete()
        messages.success(request, '資料已刪除！')
        return redirect('shpr:shprList')
    ctx = {}
    ctx['shpr'] = shpr
    ctx['form'] = form
    ctx['title'] = 'Delete'
    return render(request, template_name, ctx)