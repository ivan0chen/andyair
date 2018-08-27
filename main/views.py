from django.shortcuts import render

def main(request):
    context = {'system': '空運進口提單系統'}
    return render(request, 'main/main.html', context)
