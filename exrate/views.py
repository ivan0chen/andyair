from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from exrate.models import Exrate
from exrate.forms import ExrateForm


@login_required
def exrateList(request, template_name='exrate/exrateList.html'):
    exrates = Exrate.objects.all()
    ctx = {}
    ctx['exrates'] = exrates
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def exrateCreate(request, template_name='exrate/exrateCreate.html'):
    form = ExrateForm(request.POST or None)
    if form.is_valid():
        new_obj = form.save(commit=False)
        new_obj.created_by = request.user
        new_obj.last_updated_by = request.user
        new_obj.save()
        messages.success(request, '資料已新增！')
        # return redirect('exrate:exrateUpdate', new_obj.id)
        return redirect('exrate:exrateList')
    ctx = {}
    ctx['form'] = form
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

@login_required
def exrateUpdate(request, pk, template_name='exrate/exrateUpdate.html'):
    exrate = get_object_or_404(Exrate, pk=pk)
    form = ExrateForm(request.POST or None, instance=exrate)
    if form.is_valid():
        exrate_obj = form.save(commit=False)
        exrate_obj.last_updated_by = request.user
        exrate_obj.save()
        messages.success(request, '資料已更新！')
        # return redirect('exrate:exrateUpdate', exrate.id)
        return redirect('exrate:exrateList')
    ctx = {}
    ctx['exrate'] = exrate
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

@login_required
def exrateDelete(request, pk, template_name='exrate/exrateDelete.html'):
    exrate = get_object_or_404(Exrate, pk=pk)
    form = ExrateForm(instance=exrate)
    if request.method == 'POST':
        exrate.delete()
        messages.success(request, '資料已刪除！')
        return redirect('exrate:exrateList')
    ctx = {}
    ctx['exrate'] = exrate
    ctx['form'] = form
    ctx['title'] = 'Delete'
    return render(request, template_name, ctx)
