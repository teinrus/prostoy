import datetime
from django.template import loader

from django.db.models import Count, Sum, Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from prostoy.models import *

from .forms import Otchet


def time_in_range(start, end, current):
    return start < current < end


start1 = datetime.time(8, 00, 0)
end1 = datetime.time(16, 30, 0)
end2 = datetime.time(23, 59, 0)
current = datetime.datetime.now().time()


def index(request):
    if request.method == 'GET':

        if start1 <= datetime.datetime.now().time() <= end1:

            plan = 31500
            table = Table5.objects.filter(startdata=datetime.date.today(),
                                          starttime__gte=datetime.time(8),
                                          starttime__lte=datetime.time(16, 30))
            speed = speed5.objects.filter(data=datetime.date.today(),
                                          time__gte=datetime.time(8),
                                          time__lte=datetime.time(16, 30))
            boom= bottleExplosion.objects.filter(data=datetime.date.today(),
                                          time__gte=datetime.time(8),
                                          time__lte=datetime.time(16, 30))

        elif end1 <= datetime.datetime.now().time() <= end2:

            plan = 27000
            table = Table5.objects.filter(startdata=datetime.date.today(),
                                          starttime__gte=datetime.time(16, 29),
                                          starttime__lte=datetime.time(23, 59))
            speed = speed5.objects.filter(data=datetime.date.today(),
                                          time__gte=datetime.time(16, 29),
                                          time__lte=datetime.time(23, 59))
            boom = bottleExplosion.objects.filter(data=datetime.date.today(),
                                          time__gte=datetime.time(16, 29),
                                          time__lte=datetime.time(23, 59))
        else:
            plan = 29000
            table = Table5.objects.filter(startdata=datetime.date.today(),
                                          starttime__gte=datetime.time(00, 00),
                                          starttime__lte=datetime.time(8, 0))
            speed = speed5.objects.filter(data=datetime.date.today(),
                                          time__gte=datetime.time(00, 00),
                                          time__lte=datetime.time(8, 0))
            boom = bottleExplosion.objects.filter(data=datetime.date.today(),
                                          time__gte=datetime.time(16, 29),
                                          time__lte=datetime.time(23, 59))

    lableChart = []
    dataChart = []
    try:
        avgSpeed = round(speed.aggregate(Avg('speed')).get('speed__avg'), 2)
    except:
        avgSpeed = 0
    try:
        sumProstoy = table.aggregate(Sum('prostoy')).get('prostoy__sum')
    except:
        sumProstoy = 0
    try:
        allProduct = round(speed.aggregate(Sum('speed')).get('speed__sum') / 20, 2)
        allProc = round(allProduct / plan * 100, 2)

    except:
        allProduct = 0
        allProc = 0
    try:
        boomOut = boom.aggregate(Sum('bottle')).get('bottle__sum')
    except:
        boomOut=0

    for sp in speed:
        lableChart.append(str(sp.time))
        dataChart.append(sp.speed)
    otv_p = otv_pod.objects.all()
    #prich = list(prichina.objects.all().values_list())
    prich = list(prichina.objects.all().values())



    uch = uchastok.objects.all()
    return render(request, "index.html", {
        'table': table,
        'speed': speed,

        'lableChart': lableChart,
        'dataChart': dataChart,

        'sumProstoy': sumProstoy,
        'avgSpeed': avgSpeed,
        'allProduct': allProduct,
        'allProc': allProc,
        'boomOut':boomOut,

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
    except:
        boomOut=0
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

    otv_p = otv_pod.objects.all()
    uch = uchastok.objects.all()
    prich = prichina.objects.all()

    return render(request, "otchet.html", {
        'table': table,
        'form': form,

        'sumProstoy': sumProstoy,
        'avgSpeed': avgSpeed,
        'boomOut':boomOut,

        'lableChart': lableChart,
        'dataChart': dataChart,


        'otv_p': otv_p,
        'prich': prich,
        'uch': uch,

    })


def getData(requst):
    table = Table5.objects.all()

    return JsonResponse({"data": list(table.values())})


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
