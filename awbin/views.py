from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
import json
from django.contrib.auth.decorators import login_required
from awbin.models import Mawbin, Hawbin, Acctin, Rmkin
from awbin.forms import MawbinForm, HawbinForm, DebitForm, CreditForm, RemarkForm
from exrate.models import Exrate
from inprmk.models import Inprmk


@login_required
def mawbinList(request, template_name='awbin/mawbinList.html'):
    mawbins = Mawbin.objects.all()
    ctx = {}
    ctx['mawbins'] = mawbins
    ctx['title'] = 'MAWB List'
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
    currency_list = getCurrency()
    ctx['currency_list'] = json.dumps(currency_list)
    ctx['title'] = 'MAWB New'
    return render(request, template_name, ctx)

@login_required
def mawbinView(request, pk, template_name='awbin/mawbinView.html'):
    mawbin = get_object_or_404(Mawbin, pk=pk)
    form = MawbinForm(instance=mawbin)
    ctx = {}
    ctx['mawbin'] = mawbin
    ctx['form'] = form
    ctx['title'] = 'MAWB View'
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
    ctx['debits'] = Acctin.objects.filter(Q(mawb=mawbin) & Q(dc='D'))
    ctx['credits'] = Acctin.objects.filter(Q(mawb=mawbin) & Q(dc='C'))
    ctx['remarks'] = Rmkin.objects.filter(mawb=mawbin)
    ctx['cods'] = Hawbin.objects.filter(mawb=mawbin)
    ctx['form'] = form
    # currency_list = {"USD": "USD", "EUR": "EUR", "TWD": "TWD"}
    currency_list = getCurrency()
    remark_list = getRemark()
    ctx['currency_list'] = json.dumps(currency_list)
    ctx['remark_list'] = json.dumps(remark_list)
    ctx['title'] = 'MAWB Edit'
    return render(request, template_name, ctx)

def getCurrency():
    curr_data = Exrate.objects.all()
    currDict = {}
    for curr in curr_data:
        currDict[curr.code] = curr.code
    print(currDict)
    return currDict

def getRemark():
    rmk_data = Inprmk.objects.all()
    rmkDict = {}
    for rmk in rmk_data:
        rmkDict[rmk.code] = rmk.code
    print(rmkDict)
    return rmkDict

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
    ctx['title'] = 'MAWB Delete'
    return render(request, template_name, ctx)

@login_required
def hawbinList(request, parent_pk, template_name='awbin/hawbinList.html'):
    mawbin = get_object_or_404(Mawbin, pk=parent_pk)
    hawbins = Hawbin.objects.filter(mawb=mawbin)
    ctx = {}
    ctx["mawbin"] = mawbin
    ctx['hawbins'] = hawbins
    ctx['title'] = 'HAWB List'
    return render(request, template_name, ctx)

@login_required
def hawbinCreate(request, parent_pk, template_name='awbin/hawbinForm.html'):
    mawbin = get_object_or_404(Mawbin, pk=parent_pk)
    form = HawbinForm(request.POST or None)
    if form.is_valid():
        new_hawb = form.save(commit=False)
        new_hawb.mawb = mawbin
        new_hawb.created_by = request.user
        new_hawb.last_updated_by = request.user
        new_hawb.save()
        messages.success(request, '資料已新增！')
        return redirect('awbin:hawbinUpdate', new_hawb.id)
        # return redirect('awbin:mawbinList')
    ctx = {}
    ctx["mawbin"] = mawbin
    ctx['form'] = form
    ctx['title'] = 'HAWB New'
    return render(request, template_name, ctx)

@login_required
def hawbinView(request, pk, template_name='awbin/hawbinView.html'):
    hawbin = get_object_or_404(Hawbin, pk=pk)
    form = HawbinForm(instance=hawbin)
    ctx = {}
    ctx['hawbin'] = hawbin
    ctx['form'] = form
    ctx['title'] = 'HAWB View'
    return render(request, template_name, ctx)

@login_required
def hawbinUpdate(request, pk, template_name='awbin/hawbinForm.html'):
    hawbin = get_object_or_404(Hawbin, pk=pk)
    form = HawbinForm(request.POST or None, instance=hawbin)
    if form.is_valid():
        hawbin_obj = form.save(commit=False)
        hawbin_obj.last_updated_by = request.user
        hawbin_obj.save()
        messages.success(request, '資料已更新！')
        # return redirect('awbin:hawbinUpdate', hawbin.id)
        return redirect('awbin:mawbinList')
    ctx = {}
    ctx['hawbin'] = hawbin
    ctx['form'] = form
    ctx['title'] = 'HAWB Edit'
    return render(request, template_name, ctx)

@login_required
def hawbinDelete(request, pk, template_name='awbin/hawbinDelete.html'):
    hawbin = get_object_or_404(Hawbin, pk=pk)
    form = HawbinForm(instance=hawbin)
    if request.method == 'POST':
        hawbin.delete()
        messages.success(request, '資料已刪除！')
        return redirect('awbin:mawbinList')
    ctx = {}
    ctx['hawbin'] = hawbin
    ctx['form'] = form
    ctx['title'] = 'HAWB Delete'
    return render(request, template_name, ctx)

@login_required
def dbnoteNew(request, parent_pk, template_name='awbin/dbnoteNew.html'):
    mawbin = get_object_or_404(Mawbin, pk=parent_pk)
    form = DebitForm(request.POST or None)
    ctx = {}
    if request.method == 'POST':
        result = 'Failure'
        if form.is_valid():
            dbnote = form.save(commit=False)
            dbnote.mawb = mawbin
            dbnote.dc = 'D'
            dbnote.created_by = request.user
            dbnote.last_updated_by = request.user
            dbnote.save()
            result = 'Success'
            messages.success(request, 'Debit資料已新增！')
            # return redirect('awbin:mawbinUpdate', parent_pk)
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
    ctx = {}
    ctx["form"] = form
    ctx["mawbin"] = mawbin
    ctx['debits'] = Acctin.objects.filter(Q(mawb=mawbin) & Q(dc='D'))
    ctx["dbnCount"] = ctx['debits'].count() + 1
    ctx['title'] = ' New Debit'
    return render(request, template_name, ctx)

@login_required
def debitTabledit(request):
    if request.method == 'POST':
        debit = get_object_or_404(Acctin, pk=request.POST.get('id'))
        if request.POST.get('action') == 'edit':
            debit.dcno = request.POST.get('dcno')
            debit.dccurn = request.POST.get('dccurn')
            debit.dcamt = request.POST.get('dcamt')
            debit.last_updated_by = request.user
            debit.save()
            messages.success(request, 'Debit資料已更新！')
        if request.POST.get('action') == 'delete':
            debit.delete()
            messages.success(request, 'Debit資料已刪除！')

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
    else:
        return render(request, 'main/main.html')

@login_required
def cdnoteNew(request, parent_pk, template_name='awbin/cdnoteNew.html'):
    mawbin = get_object_or_404(Mawbin, pk=parent_pk)
    form = CreditForm(request.POST or None)
    ctx = {}
    if request.method == 'POST':
        result = 'Failure'
        if form.is_valid():
            cdnote = form.save(commit=False)
            cdnote.mawb = mawbin
            cdnote.dc = 'C'
            cdnote.created_by = request.user
            cdnote.last_updated_by = request.user
            cdnote.save()
            result = 'Success'
            print(cdnote)
            messages.success(request, 'Credit資料已新增！')
            # return redirect('awbin:mawbinUpdate', parent_pk)
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
    ctx = {}
    ctx["form"] = form
    ctx["mawbin"] = mawbin
    ctx['credits'] = Acctin.objects.filter(Q(mawb=mawbin) & Q(dc='C'))
    ctx["cdnCount"] = ctx['credits'].count() + 1
    ctx['title'] = ' New Credit'
    return render(request, template_name, ctx)

@login_required
def creditTabledit(request):
    if request.method == 'POST':
        credit = get_object_or_404(Acctin, pk=request.POST.get('id'))
        if request.POST.get('action') == 'edit':
            credit.dcno = request.POST.get('dcno')
            credit.dccurn = request.POST.get('dccurn')
            credit.dcamt = request.POST.get('dcamt')
            credit.last_updated_by = request.user
            credit.save()
            messages.success(request, 'Credit資料已更新！')
        if request.POST.get('action') == 'delete':
            credit.delete()
            messages.success(request, 'Credit資料已刪除！')

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
    else:
        return render(request, 'main/main.html')

@login_required
def remarkNew(request, parent_pk, template_name='awbin/remarkNew.html'):
    mawbin = get_object_or_404(Mawbin, pk=parent_pk)
    form = RemarkForm(request.POST or None)
    ctx = {}
    if request.method == 'POST':
        result = 'Failure'
        if form.is_valid():
            remark = form.save(commit=False)
            remark.mawb = mawbin
            remark.created_by = request.user
            remark.last_updated_by = request.user
            remark.save()
            result = 'Success'
            messages.success(request, 'Remark資料已新增！')
            # return redirect('awbin:mawbinUpdate', parent_pk)
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
    ctx = {}
    ctx["form"] = form
    ctx["mawbin"] = mawbin
    ctx['remarks'] = Rmkin.objects.filter(mawb=mawbin)
    ctx["rmkCount"] = ctx['remarks'].count() + 1
    ctx['title'] = ' New Remark'
    return render(request, template_name, ctx)

@login_required
def remarkTabledit(request):
    if request.method == 'POST':
        remark = get_object_or_404(Rmkin, pk=request.POST.get('id'))
        if request.POST.get('action') == 'edit':
            # remark.hawb = request.POST.get('hawb')
            remark.codr = request.POST.get('codr')
            # remark.statement = request.POST.get('statement')
            remark.last_updated_by = request.user
            remark.save()
            messages.success(request, 'Remark資料已更新！')
        if request.POST.get('action') == 'delete':
            remark.delete()
            messages.success(request, 'Remark資料已刪除！')

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
    else:
        return render(request, 'main/main.html')

@login_required
def codTabledit(request):
    if request.method == 'POST':
        cod = get_object_or_404(Hawbin, pk=request.POST.get('id'))
        if request.POST.get('action') == 'edit':
            cod.codcurn = request.POST.get('codcurn')
            cod.codamt = request.POST.get('codamt')
            cod.codrcvdd = request.POST.get('codrcvdd')
            cod.codpaydd = request.POST.get('codpaydd')
            cod.last_updated_by = request.user
            cod.save()
            messages.success(request, 'COD資料已更新！')
        if request.POST.get('action') == 'delete':
            cod.delete()
            messages.success(request, 'COD資料已刪除！')

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
    else:
        return render(request, 'main/main.html')