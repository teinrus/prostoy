import datetime

from django.contrib.auth.views import LoginView
from django.template import loader

from django.db.models import Count, Sum, Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from prostoy.models import *

from .forms import Otchet

start1 = datetime.time(8, 00, 0)
start2 = datetime.time(16, 30, 0)
start3 = datetime.time(23, 59, 0)


if start1 <= datetime.datetime.now().time() <= start2:
    startSmena = datetime.time(8, 00, 0)
    spotSmena =datetime.time(16, 30, 0)
elif start2 <= datetime.datetime.now().time() <= start3:
    startSmena = datetime.time(16, 30, 0)
    spotSmena =  datetime.time(23, 59, 0)
else:
    startSmena = datetime.time(00, 00, 00)
    spotSmena =  datetime.time(8, 00, 00)






def proc(startSmena, spotSmena, plan, colProduct):
    today = datetime.date.today()
    # количество продукции вып в сек
    d_start1 = datetime.datetime.combine(today, startSmena)
    d_end1 = datetime.datetime.combine(today, spotSmena)
    diff1 = d_end1 - d_start1
    planProdSec = int(plan / int(diff1.total_seconds()))

    # количество времени которое прошло
    d_start2 = datetime.datetime.combine(today, startSmena)
    d_end2 = datetime.datetime.combine(today, datetime.datetime.now().time())
    diff2 = d_end2 - d_start2

    # проц вып продукции
    return int(colProduct / ((int(diff2.total_seconds()) * planProdSec) / 100))


def index(request):
    if request.method == 'GET':
        table = Table5.objects.filter(startdata=datetime.date.today(),
                                      starttime__gte=startSmena,
                                      starttime__lte=spotSmena)
        speed = speed5.objects.filter(data=datetime.date.today(),
                                      time__gte=startSmena,
                                      time__lte=spotSmena)

    otv_p = otv_pod.objects.all()

    prich = list(prichina.objects.all().values())

    uch = uchastok.objects.all()
    return render(request, "index.html", {
        'table': table,
        'speed': speed,

        'otv_p': otv_p,
        'prich': prich,
        'uch': uch,

    })


def otchet(request):
    form = Otchet(request.GET)
    if form.is_valid():
        # Сортировка по дате
        if form.cleaned_data["start_data"] and form.cleaned_data["finish_data"]:
            if form.cleaned_data["SmenaF"]:
                if form.cleaned_data["SmenaF"] == 'Smena 0':
                    table = Table5.objects.filter(starttime__gte=datetime.time(0),
                                                  starttime__lte=datetime.time(23, 59),
                                                  startdata__gte=form.cleaned_data["start_data"],
                                                  startdata__lte=form.cleaned_data["finish_data"]
                                                  ).order_by('startdata', 'starttime')

                    speed = speed5.objects.filter(data__gte=form.cleaned_data["start_data"],
                                                  data__lte=form.cleaned_data["finish_data"],
                                                  time__gte=datetime.time(0),
                                                  time__lte=datetime.time(23, 59))
                    boom = bottleExplosion.objects.filter(data__gte=form.cleaned_data["start_data"],
                                                          data__lte=form.cleaned_data["finish_data"],
                                                          time__gte=datetime.time(0),
                                                          time__lte=datetime.time(23, 59))
                if form.cleaned_data["SmenaF"] == 'Smena 1':
                    table = Table5.objects.filter(starttime__gte=datetime.time(8),
                                                  starttime__lte=datetime.time(16, 30),
                                                  startdata__gte=form.cleaned_data["start_data"],
                                                  startdata__lte=form.cleaned_data["finish_data"]
                                                  ).order_by('startdata', 'starttime')
                    speed = speed5.objects.filter(data__gte=form.cleaned_data["start_data"],
                                                  data__lte=form.cleaned_data["finish_data"],
                                                  time__gte=datetime.time(8),
                                                  time__lte=datetime.time(16, 30))
                    boom = bottleExplosion.objects.filter(data__gte=form.cleaned_data["start_data"],
                                                          data__lte=form.cleaned_data["finish_data"],
                                                          time__gte=datetime.time(8),
                                                          time__lte=datetime.time(16, 30))
                if form.cleaned_data["SmenaF"] == 'Smena 2':
                    table = Table5.objects.filter(starttime__gte=datetime.time(16, 30),
                                                  starttime__lte=datetime.time(23, 59),
                                                  startdata__gte=form.cleaned_data["start_data"],
                                                  startdata__lte=form.cleaned_data["finish_data"]
                                                  ).order_by('startdata', 'starttime')
                    speed = speed5.objects.filter(data__gte=form.cleaned_data["start_data"],
                                                  data__lte=form.cleaned_data["finish_data"],
                                                  time__gte=datetime.time(16, 30),
                                                  time__lte=datetime.time(23, 59))
                    boom = bottleExplosion.objects.filter(data__gte=form.cleaned_data["start_data"],
                                                          data__lte=form.cleaned_data["finish_data"],
                                                          time__gte=datetime.time(16, 30),
                                                          time__lte=datetime.time(23, 59))
                if form.cleaned_data["SmenaF"] == 'Smena 3':
                    table = Table5.objects.filter(starttime__gte=datetime.time(00, 00),
                                                  starttime__lte=datetime.time(8, 00),
                                                  startdata__gte=form.cleaned_data["start_data"],
                                                  startdata__lte=form.cleaned_data["finish_data"]
                                                  ).order_by('startdata', 'starttime')
                    speed = speed5.objects.filter(data__gte=form.cleaned_data["start_data"],
                                                  data__lte=form.cleaned_data["finish_data"],
                                                  time__gte=datetime.time(00, 00),
                                                  time__lte=datetime.time(8, 00))
                    boom = bottleExplosion.objects.filter(data__gte=form.cleaned_data["start_data"],
                                                          data__lte=form.cleaned_data["finish_data"],
                                                          time__gte=datetime.time(00, 00),
                                                          time__lte=datetime.time(8, 00))
        # Сортировка по сменам:

    lableChart = []
    dataChart = []

    try:
        boomOut = boom.aggregate(Sum('bottle')).get('bottle__sum')
        if (boomOut == None):
            boomOut = 0
    except:
        boomOut = 0
    try:
        sumProstoy = table.aggregate(Sum('prostoy')).get('prostoy__sum')
    except:
        table = []
        sumProstoy = 0
    try:
        avgSpeed = round(speed.aggregate(Avg('speed')).get('speed__avg'), 2)
    except:
        avgSpeed = 0
    try:
        for sp in speed:
            lableChart.append(str(sp.time))
            dataChart.append(sp.speed)
    except:
        lableChart = []
        dataChart = []

    try:
        allProc = round((round(speed.aggregate(Sum('speed')).get('speed__sum') / 20, 2)))
    except:
        allProc = 0



    otv_p = otv_pod.objects.all()
    uch = uchastok.objects.all()
    prich = list(prichina.objects.all().values())


    return render(request, "otchet.html", {
        'table': table,
        'form': form,

        'sumProstoy': sumProstoy,
        'avgSpeed': avgSpeed,
        'boomOut': boomOut,
        'allProc':allProc,

        'lableChart': lableChart,
        'dataChart': dataChart,

        'otv_p': otv_p,
        'prich': prich,
        'uch': uch,



    })


def update_items(request):

    table5 = Table5.objects.filter(startdata=datetime.date.today(),
                                   starttime__gte=startSmena,
                                   starttime__lte=spotSmena)

    list = []
    for table in table5:
        table_info = {
            'id': table.id,
            'startdata': table.startdata,
            'starttime': table.starttime,
            'prostoy': table.prostoy,

            'uchastok': table.uchastok,
            'otv_pod': table.otv_pod,
            'prichina': table.prichina,
            'comment': table.comment,
        }
        list.append(table_info)

    table_dic = {}
    table_dic['data'] = list

    return render(request, 'table_body.html', {'table5': table5})


def getData(requst):

    plan = 31500

    if start1 <= datetime.datetime.now().time() <= start2:
        startSmena = datetime.time(8, 00, 0)
        spotSmena = datetime.time(16, 30, 0)
    elif start2 <= datetime.datetime.now().time() <= start3:
        startSmena = datetime.time(16, 30, 0)
        spotSmena = datetime.time(23, 59, 0)
    else:
        startSmena = datetime.time(00, 00, 00)
        spotSmena = datetime.time(8, 00, 00)



    table = Table5.objects.filter(startdata=datetime.date.today(),
                                  starttime__gte=startSmena,
                                  starttime__lte=spotSmena)
    speed = speed5.objects.filter(data=datetime.date.today(),
                                  time__gte=startSmena,
                                  time__lte=spotSmena)
    boom = bottleExplosion.objects.filter(data=datetime.date.today(),
                                          time__gte=startSmena,
                                          time__lte=spotSmena)


    try:
        avgSpeed = round(speed.aggregate(Avg('speed')).get('speed__avg'), 2)
    except:
        avgSpeed = 0
    try:
        sumProstoy = table.aggregate(Sum('prostoy')).get('prostoy__sum')

        if (sumProstoy == None):
            sumProstoy = '00:00'
    except:
        sumProstoy = '00:00'
    try:
        product = round((round(speed.aggregate(Sum('speed')).get('speed__sum') / 20, 2)))
        allProc=proc(startSmena, spotSmena, plan, product),
    except:
        product = 0
        allProc=0
    try:
        boomOut = boom.aggregate(Sum('bottle')).get('bottle__sum')
        if (boomOut == None):
            boomOut = 0
    except:
        boomOut = 0

    lableChart = []
    dataChart = []

    for sp in speed:
        lableChart.append(str(sp.time))
        dataChart.append(sp.speed)

    result = {"allProc": allProc,
              "boomOut": boomOut,
              'sumProstoy': str(sumProstoy),
              'avgSpeed': avgSpeed,
              'lableChart': lableChart,
              'dataChart': dataChart,

              }
    return JsonResponse(result)


def update(request):
    if request.method == 'POST':

        pk = request.POST.get('pk')
        name = request.POST.get('name')
        v = request.POST.get('value')

        if name == 'uchastok':
            try:
                a = Table5.objects.get(id=pk)
                a.uchastok = v
                a.save()
            except:
                a = Table5(uchastok=v, id=pk)
                a.save()
        elif name == 'prichina':
            try:

                a = Table5.objects.get(id=pk)
                a.prichina = v
                a.save()
            except:
                a = Table5(prichina=v, id=pk)
                a.save()
        elif name == 'otv_pod':
            try:
                a = Table5.objects.get(id=pk)
                a.otv_pod = v
                a.save()
            except:
                a = Table5(otv_pod=v, id=pk)
                a.save()
        elif name == 'comment':
            try:
                a = Table5.objects.get(id=pk)
                a.comment = v
                a.save()
            except:
                a = Table5(comment=v, id=pk)
                a.save()

    return HttpResponse('yes')
