from django.shortcuts import render

def main(request):
    context = {'system': '空運進口提單系統'}
    context['nextURL'] = request.GET.get('next')
    return render(request, 'main/main.html', context)
