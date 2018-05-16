from django.shortcuts import render
from django.http import HttpResponse
from .models import tb_Gaget
from django.template import loader
from itertools import chain
from collections import defaultdict
from .tables import InstrumentTables
from django_tables2 import RequestConfig
from django_tables2.utils import AttributeDict
from django.template import RequestContext
import json
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .forms import AddGagetForm
from django.shortcuts import redirect

@cache_page(60 * 15)
@csrf_protect
@csrf_exempt

def instrumentos(request):
    all_instrumentos = tb_Gaget.objects.all()
    tables = InstrumentTables(tb_Gaget.objects.all())
    # print(tables.data)
    RequestConfig(request).configure(tables)

    return render(request, 'teste.html', {'table': tables})

def add_gaget(request):

    if request.method == "POST":
        form = AddGagetForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return render(request, 'teste1.html')
        else:
            print(form.errors)

    else:
        form = AddGagetForm()
        # Instrumento = request.POST.get('eqp_select')
        # Fabricante = request.POST.get('fabricante-input')
        # Modelo = request.POST.get('modelo-input')
        # Serial = request.POST.get('serial-input')
        # Slope = request.POST.get('slope-input')
        # Offset = request.POST.get('offset-input')
        # Calibracao = request.POST.get('calibracao-input')
        #
        # context = {'Tipo': Instrumento, 'Fabricante': Fabricante, 'Modelo': Modelo, 'Serial': Serial, 'Slope': Slope, 'Offset': Offset, 'Calibracao': Calibracao}

        print(form)
    return render(request, 'teste1.html', {'form': form})

# Create your views here.
def detail(request, instrumento_id):
    # try:
    #     print(poll_id)
    #     p = tb_Gaget.objects.get(pk=poll_id)
    # except tb_Gaget.DoesNotExist:
    #     raise render('Portal_Asset/template/404.html')
    # table = tb_Gaget.objects.all()
    # template = loader.get_template('index.html')
    print(instrumento_id)
    return HttpResponse("<h2>Instrumento id: " + str(instrumento_id) + "</h2>")
    # return render(request, 'template/index.html', {'gagets': tb_Gaget.objects.all()})