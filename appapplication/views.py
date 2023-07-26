from django.shortcuts import render

# 모델 클래스 import
from appapplication.models import Bottle

def index(request):
    #전체 데이터 가져오기
    data = Bottle.objects.all()
    for t in data:
        print(t)
    #data = bottle.objects.all(bottle)
    #ata = bottle.objects.filtter(bottleid= '1')
    return render(request, 'index.html', {'data': data})

def detail(request, bottleid):
    bottle = Bottle.objects.get(bottleid = bottleid)
    print(bottle)
    return render(request, 'detail.html', {'bottle': bottle})
