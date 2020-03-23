from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime
from .models import *

# def xmlout_14(request):
#     latest_match_list = Match.objects.all().order_by('-pub_date')
#     taikai_list = Eventinfo.objects.all()   
#     context = {
#         'latest_match_list': latest_match_list,
#         'taikai_list': taikai_list,
#     }
#     t = loader.get_template('app_sumo/os14.xml')
#     return HttpResponse(t.render(context), content_type='text/xml; charset=utf-8')

def xmlout_14(request):
    response = HttpResponse(content_type='text/xml; charset=utf-8')
    response['Content-Disposition'] =  'attachment; filename=test.xml'

    latest_match_list = Match.objects.all().order_by('-pub_date')
    taikai_list = Eventinfo.objects.all()
    t = loader.get_template('app_sumo/os14.xml')
    context = {
        'latest_match_list': latest_match_list,
        'taikai_list': taikai_list,
    }

    response.write(t.render(context))
    return response



# def input14(request):
#     d = {
#         'matchlist': Match.objects.all(),
#     }
#     return render(request, 'app_sumo/input14.html', d)

# def update14(request):
#     d = {
#         'matchlist': Match.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date'),
#     }
#     return render(request, 'app_sumo/update14.html', d)

# def update14_new(request):
#     if request.method == "POST":
#         form = MatchForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.pub_date = timezone.now()
#             post.save()
#             return redirect('update14')
#     else:
#         form = MatchForm()
#     return render(request, 'app_sumo/update14_edit.html', {'form': form})