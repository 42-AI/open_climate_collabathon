from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You are at the map index.")

### Plotly part ###
from django.views.generic import TemplateView
from . import draw_map

class MapView(TemplateView):
    template_name = 'map.html'
    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['map'] = draw_map.draw_map()
        return context
