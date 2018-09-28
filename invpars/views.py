from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from invpars.models import Invpars, Invstk
from invpars.forms import InvparsForm, InvstkForm

@login_required
def invparsList(request, template_name='invpars/invparsList.html'):
    invparss = Invpars.objects.all()
    ctx = {}
    ctx['invparss'] = invparss
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def invparsView(request, pk, template_name='invpars/invparsView.html'):
    invpars = get_object_or_404(Invpars, pk=pk)
    ctx = {}
    ctx['invpars'] = invpars
    ctx['invstks'] = Invstk.objects.filter(invpars=invpars)
    ctx['title'] = 'View'
    return render(request, template_name, ctx)

@login_required
def invparsUpdate(request, pk, template_name='invpars/invparsForm.html'):
    invpars = get_object_or_404(Invpars, pk=pk)
    form = InvparsForm(request.POST or None, instance=invpars)
    if form.is_valid():
        invpars_obj = form.save(commit=False)
        invpars_obj.last_updated_by = request.user
        invpars.save()
        messages.success(request, '資料已更新！')
        return redirect('invpars:invparsUpdate', invpars.id)
    ctx = {}
    ctx['invpars'] = invpars
    ctx['invstks'] = Invstk.objects.filter(invpars=invpars)
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)

@login_required
def invstkNew(request, parent_pk, template_name='invpars/invstkNew.html'):
    invpars = get_object_or_404(Invpars, pk=parent_pk)
    form = InvstkForm(request.POST or None)
    if form.is_valid():
        invstk = form.save(commit=False)
        invstk.invpars = invpars
        invstk.created_by = request.user
        invstk.last_updated_by = request.user
        invstk.save()
        messages.success(request, '明細資料已新增！')
        return redirect('invpars:invparsUpdate', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["invpars"] = invpars
    ctx['invstks'] = Invstk.objects.filter(invpars=invpars)
    ctx['title'] = ' New Detail'
    return render(request, template_name, ctx)

@login_required
def invstkTabledit(request):
    if request.method == 'POST':
        invstk = get_object_or_404(Invstk, pk=request.POST.get('id'))
        if request.POST.get('action') == 'edit':
            invstk.invyymm = request.POST.get('invyymm')
            invstk.invchar = request.POST.get('invchar')
            invstk.sttno = request.POST.get('sttno')
            invstk.endno = request.POST.get('endno')
            invstk.nowno = request.POST.get('nowno')
            invstk.usedd = datetime.strptime(request.POST.get('usedd'),"%Y-%m-%d").date()
            invstk.boxno = request.POST.get('boxno')
            invstk.machno = request.POST.get('machno')
            invstk.last_updated_by = request.user
            invstk.save()
            messages.success(request, '明細資料已更新！')
        if request.POST.get('action') == 'delete':
            invstk.delete()
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



