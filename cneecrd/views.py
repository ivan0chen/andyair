from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from cneecrd.models import Cneecrd
from custcsn.models import Custcsn
from cneecrd.forms import CneecrdForm


@login_required
def cneecrdList(request, template_name='cneecrd/cneecrdList.html'):
    cneecrds = Custcsn.objects.all().prefetch_related('cneecrd_custcsn')
    ctx = {}
    ctx['cneecrds'] = cneecrds
    ctx['title'] = 'List'
    return render(request, template_name, ctx)

@login_required
def cneecrdUpdate(request, pk, template_name='cneecrd/cneecrdUpdate.html'):
    cneecrd = get_object_or_404(Cneecrd, pk=pk)
    form = CneecrdForm(request.POST or None, instance=cneecrd)
    ctx = {}
    if request.method == 'POST':
        result = 'Failure'
        if form.is_valid():
            if (float(request.POST.get('crdamt')) >= (float(request.POST.get('aro'))+float(request.POST.get('ars'))+float(request.POST.get('arc')))):
                cneecrd_obj = form.save(commit=False)
                cneecrd_obj.last_updated_by = request.user
                cneecrd_obj.save()
                result = 'Success'
                messages.success(request, '資料已更新！')
                # return redirect('cneecrd:cneecrdUpdate', cneecrd.id)
                # return redirect('cneecrd:cneecrdList')
            else:
                messages.warning(request, '輸入錯誤！ 信用額度（總）不得小於 出口應收+進口發單應收+進口報關應收')
        else:
            messages.success(request, '資料輸入錯誤，請更正！')
        django_messages = []
        for message in messages.get_messages(request):
            django_messages.append({
                "level": message.level,
                "message": message.message,
                "tags": message.tags,
            })

        ctx['request'] = request.POST
        ctx['result'] = result
        ctx['messages'] = django_messages
        return JsonResponse(ctx)

    ctx['cneecrd'] = cneecrd
    ctx['form'] = form
    ctx['title'] = 'Edit'
    return render(request, template_name, ctx)
