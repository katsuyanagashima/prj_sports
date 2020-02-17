from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from datetime import datetime

import csv
from io import TextIOWrapper, StringIO
from .models import csvtest1, auto_schedule, systemstatus
from .forms import Csvtest1Form

# from .import check_receiving_autorace

def index(request):
    template = loader.get_template('app_autorace/index.html')
    context = {
       'status':systemstatus.objects.last(),
    #    'status':systemstatus.objects.latest(sys_updated.fields),
    }
    return HttpResponse(template.render(context, request))

def unyou(request):
    template = loader.get_template('app_autorace/unyou.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def master(request):
    template = loader.get_template('app_autorace/master.html')
    context = {
    }
    return HttpResponse(template.render(context, request))



def upload1(request):
    csv1 = csvtest1()
    # form = Csvtest1Form()
    d = {
        'data':csvtest1.objects.all(),
        }
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            csv1, created = csvtest1.objects.get_or_create(name=line[0])
            csv1.no = line[0]
            csv1.name = line[1]
            csv1.save()
        
        return render(request, 'app_autorace/upload1.html', d)

    else:
        return render(request, 'app_autorace/upload1.html', d)

#スケジュールデータ
def upload_schedule(request):
    csv2 = auto_schedule()
    d = {
        'data':auto_schedule.objects.all(),
        }
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data, skipinitialspace=True)
        for line in csv_file:
            csv2, created = auto_schedule.objects.get_or_create(pk=line[3])
            csv2.kind = line[0]
            csv2.kindofdata = line[1]
            csv2.dateofsend = line[2]
            csv2.dateofrace1 = line[3]
            csv2.placeofrace1 = line[4]
            csv2.place_code1_1 = line[5]
            csv2.numberofrace1_1 = line[6]
            csv2.place_code1_2 = line[7]    
            csv2.numberofrace1_2 = line[8]
            csv2.place_code1_3 = line[9]
            csv2.numberofrace1_3 = line[10]
            csv2.place_code1_4 = line[11]
            csv2.numberofrace1_4 = line[12]
            csv2.place_code1_5 = line[13]
            csv2.numberofrace1_5 = line[14]
            csv2.place_code1_6 = line[15]
            csv2.numberofrace1_6 = line[16]
            csv2.dateofrace2 = line[17]
            csv2.placeofrace2 = line[18]
            csv2.place_code2_1 = line[19]
            csv2.numberofrace2_1 = line[20]
            csv2.place_code2_2 = line[21]
            csv2.numberofrace2_2 = line[22]
            csv2.place_code2_3 = line[23]
            csv2.numberofrace2_3 = line[24]
            csv2.place_code2_4 = line[25]
            csv2.numberofrace2_4 = line[26]
            csv2.place_code2_5 = line[27]
            csv2.numberofrace2_5 = line[28]
            csv2.place_code2_6 = line[29]
            csv2.numberofrace2_6 = line[30]
            csv2.dateofrace3 = line[31]
            csv2.placeofrace3= line[32]
            csv2.place_code3_1 = line[33]
            csv2.numberofrace3_1 = line[34]
            csv2.place_code3_2 = line[35]
            csv2.numberofrace3_2 = line[36]
            csv2.place_code3_3 = line[37]
            csv2.numberofrace3_3 = line[38]
            csv2.place_code3_4 = line[39]
            csv2.numberofrace3_4 = line[40]
            csv2.place_code3_5 = line[41]
            csv2.numberofrace3_5 = line[42]
            csv2.place_code3_6 = line[43]
            csv2.numberofrace3_6 = line[44]
            csv2.prize30 = line[45]
            csv2.save()

        return render(request, 'app_autorace/upload_schedule.html', d)
    else:
        return render(request, 'app_autorace/upload_schedule.html', d)




def exec_check_receiving_autorace(request):
    file = 'C:/pg/Python38-32/prj_sports/app_autorace/check_receiving_autorace.py'
    result = check_receiving_autorace(file)