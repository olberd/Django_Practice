from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from django.http import HttpResponse
from .forms import BbForm
from .models import Bb, Rubric
from django.urls import reverse_lazy
import datetime
from django.core.paginator import Paginator


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(bbs, 3)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)

    context = {'rubrics': rubrics, 'page': page, 'bbs': page.object_list}
    return render(request, 'bboard/index.html', context)

    # date = datetime.date.today().strftime('%A %d. %B %Y')
    # s = 'Список объявлений \r\n\r\n\r\n' + date + '\r\n\r\n'
    # for bb in Bb.objects.all():
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class RubricCreate(CreateView):
    model = Rubric
    fields = ['title']




