from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime

from .models import *
from .forms import *
import csv
from io import TextIOWrapper, StringIO

#CSV検証用
def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
          BA7, created = Schedule_BA7.objects.get_or_create(Data_ID=line[1])
          BA7.Data_ID = line[0]
          BA7.held_year = line[1]
          BA7.Organizer_times = line[2]
          BA7.Track_times = line[3]
          BA7.Organizer_code = line[4]
          BA7.Track_code = line[5]
          BA7.Held_code = line[6]
          BA7.Night_game_code = line[7]
          BA7.Dates = line[8]
          BA7.Date_1 = line[9]
          BA7.Day_code_1 = line[10]
          BA7.Races_1 = line[11]
          BA7.Postpone_date_1_1 = line[12]
          BA7.Postpone_day_code_1_1 = line[13]
          BA7.Postpone_start_1_1 = line[14]
          BA7.Postpone_date_1_2 = line[15]
          BA7.Postpone_day_code_1_2 = line[16]
          BA7.Postpone_start_1_2 = line[17]
          BA7.Date_2 = line[18]
          BA7.Day_code_2 = line[19]
          BA7.Races_2 = line[20]
          BA7.Postpone_date_2_1 = line[21]
          BA7.Postpone_day_code_2_1 = line[22]
          BA7.Postpone_start_2_1 = line[23]
          BA7.Postpone_date_2_2 = line[24]
          BA7.Postpone_day_code_2_2 = line[25]
          BA7.Postpone_start_2_2 = line[26]
          BA7.Date_3 = line[27]
          BA7.Day_code_3 = line[28]
          BA7.Races_3 = line[29]
          BA7.Postpone_date_3_1 = line[30]
          BA7.Postpone_day_code_3_1 = line[31]
          BA7.Postpone_start_3_1 = line[32]
          BA7.Postpone_date_3_2 = line[33]
          BA7.Postpone_day_code_3_2 = line[34]
          BA7.Postpone_start_3_2 = line[35]
          BA7.Date_4 = line[36]
          BA7.Day_code_4 = line[37]
          BA7.Races_4 = line[38]
          BA7.Postpone_date_4_1 = line[39]
          BA7.Postpone_day_code_4_1 = line[40]
          BA7.Postpone_start_4_1 = line[41]
          BA7.Postpone_date_4_2 = line[42]
          BA7.Postpone_day_code_4_2 = line[43]
          BA7.Postpone_start_4_2 = line[44]
          BA7.Date_5 = line[45]
          BA7.Day_code_5 = line[46]
          BA7.Races_5 = line[47]
          BA7.Postpone_date_5_1 = line[48]
          BA7.Postpone_day_code_5_1 = line[49]
          BA7.Postpone_start_5_1 = line[50]
          BA7.Postpone_date_5_2 = line[51]
          BA7.Postpone_day_code_5_2 = line[52]
          BA7.Postpone_start_5_2 = line[53]
          BA7.Date_6 = line[54]
          BA7.Day_code_6 = line[55]
          BA7.Races_6 = line[56]
          BA7.Postpone_date_6_1 = line[57]
          BA7.Postpone_day_code_6_1 = line[58]
          BA7.Postpone_start_6_1 = line[59]
          BA7.Postpone_date_6_2 = line[60]
          BA7.Postpone_day_code_6_2 = line[61]
          BA7.Postpone_start_6_2 = line[62]
          BA7.save()

        return render(request, 'app_ckeiba/upload.html')

    else:
        return render(request, 'app_ckeiba/upload.html')
    

#CSV検証用（パターン２）
def upload2(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
          BA7, created = Schedule_BA7.objects.get_or_create(Data_ID=line[1])
          BA7.Data_ID = line[0]
          BA7.held_year = line[1]
          BA7.Organizer_times = line[2]
          BA7.Track_times = line[3]
          BA7.Organizer_code = line[4]
          BA7.Track_code = line[5]
          BA7.Held_code = line[6]
          BA7.Night_game_code = line[7]
          BA7.Dates = line[8]
          BA7.Date_1 = line[9]
          BA7.Day_code_1 = line[10]
          BA7.Races_1 = line[11]
          BA7.Postpone_date_1_1 = line[12]
          BA7.Postpone_day_code_1_1 = line[13]
          BA7.Postpone_start_1_1 = line[14]
          BA7.Postpone_date_1_2 = line[15]
          BA7.Postpone_day_code_1_2 = line[16]
          BA7.Postpone_start_1_2 = line[17]
          BA7.Date_2 = line[18]
          BA7.Day_code_2 = line[19]
          BA7.Races_2 = line[20]
          BA7.Postpone_date_2_1 = line[21]
          BA7.Postpone_day_code_2_1 = line[22]
          BA7.Postpone_start_2_1 = line[23]
          BA7.Postpone_date_2_2 = line[24]
          BA7.Postpone_day_code_2_2 = line[25]
          BA7.Postpone_start_2_2 = line[26]
          BA7.Date_3 = line[27]
          BA7.Day_code_3 = line[28]
          BA7.Races_3 = line[29]
          BA7.Postpone_date_3_1 = line[30]
          BA7.Postpone_day_code_3_1 = line[31]
          BA7.Postpone_start_3_1 = line[32]
          BA7.Postpone_date_3_2 = line[33]
          BA7.Postpone_day_code_3_2 = line[34]
          BA7.Postpone_start_3_2 = line[35]
          BA7.Date_4 = line[36]
          BA7.Day_code_4 = line[37]
          BA7.Races_4 = line[38]
          BA7.Postpone_date_4_1 = line[39]
          BA7.Postpone_day_code_4_1 = line[40]
          BA7.Postpone_start_4_1 = line[41]
          BA7.Postpone_date_4_2 = line[42]
          BA7.Postpone_day_code_4_2 = line[43]
          BA7.Postpone_start_4_2 = line[44]
          BA7.Date_5 = line[45]
          BA7.Day_code_5 = line[46]
          BA7.Races_5 = line[47]
          BA7.Postpone_date_5_1 = line[48]
          BA7.Postpone_day_code_5_1 = line[49]
          BA7.Postpone_start_5_1 = line[50]
          BA7.Postpone_date_5_2 = line[51]
          BA7.Postpone_day_code_5_2 = line[52]
          BA7.Postpone_start_5_2 = line[53]
          BA7.Date_6 = line[54]
          BA7.Day_code_6 = line[55]
          BA7.Races_6 = line[56]
          BA7.Postpone_date_6_1 = line[57]
          BA7.Postpone_day_code_6_1 = line[58]
          BA7.Postpone_start_6_1 = line[59]
          BA7.Postpone_date_6_2 = line[60]
          BA7.Postpone_day_code_6_2 = line[61]
          BA7.Postpone_start_6_2 = line[62]
          BA7.save()

        return render(request, 'app_ckeiba/upload2.html')
    #    return render(request, 'app_ckeiba/upload2.html')

    else:
        return render(request, 'app_ckeiba/upload2.html')
    #    return render(request, 'app_ckeiba/upload2.html')


#開催日割_BA7 CSVファイル読み込み
def Line2Schedule_BA7(line):
    Schedule_BA7.objects.get_or_create(
    Data_ID = line[0],
    held_year = line[1],
    Organizer_times = line[2],
    Track_times = line[3],
    Organizer_code = line[4],
    Track_code = line[5],
    Held_code = line[6],
    Night_game_code = line[7],
    Dates = line[8],
    Date_1 = line[9],
    Day_code_1 = line[10],
    Races_1 = line[11],
    Postpone_date_1_1 = line[12],
    Postpone_day_code_1_1 = line[13],
    Postpone_start_1_1 = line[14],
    Postpone_date_1_2 = line[15],
    Postpone_day_code_1_2 = line[16],
    Postpone_start_1_2 = line[17],
    Date_2 = line[18],
    Day_code_2 = line[19],
    Races_2 = line[20],
    Postpone_date_2_1 = line[21],
    Postpone_day_code_2_1 = line[22],
    Postpone_start_2_1 = line[23],
    Postpone_date_2_2 = line[24],
    Postpone_day_code_2_2 = line[25],
    Postpone_start_2_2 = line[26],
    Date_3 = line[27],
    Day_code_3 = line[28],
    Races_3 = line[29],
    Postpone_date_3_1 = line[30],
    Postpone_day_code_3_1 = line[31],
    Postpone_start_3_1 = line[32],
    Postpone_date_3_2 = line[33],
    Postpone_day_code_3_2 = line[34],
    Postpone_start_3_2 = line[35],
    Date_4 = line[36],
    Day_code_4 = line[37],
    Races_4 = line[38],
    Postpone_date_4_1 = line[39],
    Postpone_day_code_4_1 = line[40],
    Postpone_start_4_1 = line[41],
    Postpone_date_4_2 = line[42],
    Postpone_day_code_4_2 = line[43],
    Postpone_start_4_2 = line[44],
    Date_5 = line[45],
    Day_code_5 = line[46],
    Races_5 = line[47],
    Postpone_date_5_1 = line[48],
    Postpone_day_code_5_1 = line[49],
    Postpone_start_5_1 = line[50],
    Postpone_date_5_2 = line[51],
    Postpone_day_code_5_2 = line[52],
    Postpone_start_5_2 = line[53],
    Date_6 = line[54],
    Day_code_6 = line[55],
    Races_6 = line[56],
    Postpone_date_6_1 = line[57],
    Postpone_day_code_6_1 = line[58],
    Postpone_start_6_1 = line[59],
    Postpone_date_6_2 = line[60],
    Postpone_day_code_6_2 = line[61],
    Postpone_start_6_2 = line[62])
