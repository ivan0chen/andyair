from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from awbin.models import Mawbin
from awbin.forms import MawbinForm


@login_required
def mawbinList(request, template_name='awbin/mawbinList.html'):
    mawbins = Mawbin.objects.all()
    ctx = {}
    ctx['mawbins'] = mawbins
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def mawbinCreate(request, template_name='awbin/mawbinForm.html'):
    form = MawbinForm(request.POST or None)
    # print(request.POST.get("mcurncy"))
    if form.is_valid():
        print(request.POST.get("mcurncy"))
        new_mawb = form.save(commit=False)
        new_mawb.created_by = request.user
        new_mawb.last_updated_by = request.user
        new_mawb.save()
        messages.success(request, '資料已新增！')
        # return redirect('awbin:mawbinUpdate', new_mawb.id)
        return redirect('awbin:mawbinList')
    ctx = {}
    ctx['form'] = form
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

@login_required
def mawbinView(request, pk, template_name='awbin/mawbinView.html'):
    mawbin = get_object_or_404(Mawbin, pk=pk)
    form = MawbinForm(instance=mawbin)
    ctx = {}
    ctx['mawbin'] = mawbin
    ctx['form'] = form
    ctx['title'] = 'View'
    return render(request, template_name, ctx)

@login_required
def mawbinUpdate(request, pk, template_name='awbin/mawbinForm.html'):
    mawbin = get_object_or_404(Mawbin, pk=pk)
    form = MawbinForm(request.POST or None, instance=mawbin)
    if form.is_valid():
        mawbin_obj = form.save(commit=False)
        mawbin_obj.last_updated_by = request.user
        mawbin_obj.save()
        messages.success(request, '資料已更新！')
        # return redirect('awbin:mawbinUpdate', mawbin.id)
        return redirect('awbin:mawbinList')
    ctx = {}
    ctx['mawbin'] = mawbin
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

@login_required
def mawbinDelete(request, pk, template_name='awbin/mawbinDelete.html'):
    mawbin = get_object_or_404(Mawbin, pk=pk)
    form = MawbinForm(instance=mawbin)
    if request.method == 'POST':
        mawbin.delete()
        messages.success(request, '資料已刪除！')
        return redirect('awbin:mawbinList')
    ctx = {}
    ctx['mawbin'] = mawbin
    ctx['form'] = form
    ctx['title'] = 'Delete'
    return render(request, template_name, ctx)