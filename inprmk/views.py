from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from inprmk.models import Inprmk
from inprmk.forms import InprmkForm


@login_required
def inprmkList(request, template_name='inprmk/inprmkList.html'):
    inprmks = Inprmk.objects.all()
    ctx = {}
    ctx['inprmks'] = inprmks
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def inprmkCreate(request, template_name='inprmk/inprmkCreate.html'):
    form = InprmkForm(request.POST or None)
    if form.is_valid():
        new_cust = form.save(commit=False)
        new_cust.created_by = request.user
        new_cust.last_updated_by = request.user
        new_cust.save()
        messages.success(request, '資料已新增！')
        # return redirect('inprmk:inprmkUpdate', new_cust.id)
        return redirect('inprmk:inprmkList')
    ctx = {}
    ctx['form'] = form
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

@login_required
def inprmkView(request, pk, template_name='inprmk/inprmkView.html'):
    inprmk = get_object_or_404(Inprmk, pk=pk)
    form = InprmkForm(instance=inprmk)
    ctx = {}
    ctx['inprmk'] = inprmk
    ctx['form'] = form
    ctx['title'] = 'View'
    return render(request, template_name, ctx)

@login_required
def inprmkUpdate(request, pk, template_name='inprmk/inprmkUpdate.html'):
    inprmk = get_object_or_404(Inprmk, pk=pk)
    form = InprmkForm(request.POST or None, instance=inprmk)
    if form.is_valid():
        cuscsn_obj = form.save(commit=False)
        cuscsn_obj.last_updated_by = request.user
        cuscsn_obj.save()
        messages.success(request, '資料已更新！')
        # return redirect('inprmk:inprmkUpdate', inprmk.id)
        return redirect('inprmk:inprmkList')
    ctx = {}
    ctx['inprmk'] = inprmk
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

@login_required
def inprmkDelete(request, pk, template_name='inprmk/inprmkDelete.html'):
    inprmk = get_object_or_404(Inprmk, pk=pk)
    form = InprmkForm(instance=inprmk)
    if request.method == 'POST':
        inprmk.delete()
        messages.success(request, '資料已刪除！')
        return redirect('inprmk:inprmkList')
    ctx = {}
    ctx['inprmk'] = inprmk
    ctx['form'] = form
    ctx['title'] = 'Delete'
    return render(request, template_name, ctx)