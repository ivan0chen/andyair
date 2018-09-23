from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from inpfee.models import Inpfee
from inpfee.forms import InpfeeForm


@login_required
def inpfeeList(request, template_name='inpfee/inpfeeList.html'):
    inpfees = Inpfee.objects.all()
    ctx = {}
    ctx['inpfees'] = inpfees
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def inpfeeCreate(request, template_name='inpfee/inpfeeCreate.html'):
    form = InpfeeForm(request.POST or None)
    if form.is_valid():
        new_cust = form.save(commit=False)
        new_cust.created_by = request.user
        new_cust.last_updated_by = request.user
        new_cust.save()
        messages.success(request, '資料已新增！')
        # return redirect('inpfee:inpfeeUpdate', new_cust.id)
        return redirect('inpfee:inpfeeList')
    ctx = {}
    ctx['form'] = form
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

@login_required
def inpfeeView(request, pk, template_name='inpfee/inpfeeView.html'):
    inpfee = get_object_or_404(Inpfee, pk=pk)
    form = InpfeeForm(instance=inpfee)
    ctx = {}
    ctx['inpfee'] = inpfee
    ctx['form'] = form
    ctx['title'] = 'View'
    return render(request, template_name, ctx)

@login_required
def inpfeeUpdate(request, pk, template_name='inpfee/inpfeeUpdate.html'):
    inpfee = get_object_or_404(Inpfee, pk=pk)
    form = InpfeeForm(request.POST or None, instance=inpfee)
    if form.is_valid():
        inpfee_obj = form.save(commit=False)
        inpfee_obj.last_updated_by = request.user
        inpfee_obj.save()
        messages.success(request, '資料已更新！')
        # return redirect('inpfee:inpfeeUpdate', inpfee.id)
        return redirect('inpfee:inpfeeList')
    ctx = {}
    ctx['inpfee'] = inpfee
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

@login_required
def inpfeeDelete(request, pk, template_name='inpfee/inpfeeDelete.html'):
    inpfee = get_object_or_404(Inpfee, pk=pk)
    form = InpfeeForm(instance=inpfee)
    if request.method == 'POST':
        inpfee.delete()
        messages.success(request, '資料已刪除！')
        return redirect('inpfee:inpfeeList')
    ctx = {}
    ctx['inpfee'] = inpfee
    ctx['form'] = form
    ctx['title'] = 'Delete'
    return render(request, template_name, ctx)