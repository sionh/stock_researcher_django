from django.shortcuts import render
from django.views import generic

from .models import Shikiho
from .forms import SearchForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'shikihos/index.html'
    context_object_name = 'result_shikihos'
    model = Shikiho
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_param = {
            'year': self.request.GET.get('year'),
            'quarter': self.request.GET.get('quarter'),
            'code': self.request.GET.get('code'),
            'comp_name': self.request.GET.get('comp_name'),
            'feature': self.request.GET.get('feature'),
            'topic': self.request.GET.get('topic'),
            'outlook': self.request.GET.get('outlook'),
        }

        search_form = SearchForm(initial = search_param)
        context['search_form'] = search_form

        return context

    def get_queryset(self):
        year = int(self.request.GET.get('year')) if self.request.GET.get('year') else 2019
        quarter = int(self.request.GET.get('quarter')) if self.request.GET.get('quarter') else 1
        shikiho = Shikiho.objects.all()
        if year:
            shikiho = shikiho.filter(year=year)
        if quarter:
            shikiho = shikiho.filter(quarter=quarter)
        if self.request.GET.get('code'):
            shikiho = shikiho.filter(code__contains=self.request.GET.get('code'))
        if self.request.GET.get('comp_name'):
            shikiho = shikiho.filter(comp_name__contains=self.request.GET.get('comp_name'))
        if self.request.GET.get('feature'):
            shikiho = shikiho.filter(feature__contains=self.request.GET.get('feature'))
        if self.request.GET.get('topic'):
            shikiho = shikiho.filter(topic__contains=self.request.GET.get('topic'))
        if self.request.GET.get('outlook'):
            shikiho = shikiho.filter(outlook__contains=self.request.GET.get('outlook'))
        
        return shikiho.order_by('code')
    