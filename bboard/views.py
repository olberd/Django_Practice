from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Bb, Rubric
import datetime


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

    # date = datetime.date.today().strftime('%A %d. %B %Y')
    # s = 'Список объявлений \r\n\r\n\r\n' + date + '\r\n\r\n'
    # for bb in Bb.objects.all():
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)
