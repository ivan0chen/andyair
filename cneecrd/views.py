from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cneecrd.models import Cneecrd
from cneecrd.forms import CneecrdForm


@login_required
def cneecrdList(request, template_name='cneecrd/cneecrdList.html'):
    cneecrds = Cneecrd.objects.all()
    ctx = {}
    ctx['cneecrds'] = cneecrds
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def cneecrdUpdate(request, pk, template_name='cneecrd/cneecrdUpdate.html'):
    cneecrd = get_object_or_404(Cneecrd, pk=pk)
    form = CneecrdForm(request.POST or None, instance=cneecrd)
    if form.is_valid():
        cneecrd_obj = form.save(commit=False)
        cneecrd_obj.last_updated_by = request.user
        cneecrd_obj.save()
        messages.success(request, '資料已更新！')
        # return redirect('cneecrd:cneecrdUpdate', cneecrd.id)
        return redirect('cneecrd:cneecrdList')
    ctx = {}
    ctx['cneecrd'] = cneecrd
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)
