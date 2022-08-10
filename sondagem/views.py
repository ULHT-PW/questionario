from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

# imports para criar qrcode 
import qrcode
import qrcode.image.svg
from io import BytesIO

# imports para imprimir grafico
from matplotlib import pyplot as plt
import io
import urllib, base64
import matplotlib
matplotlib.use('Agg')



def pergunta_view(request, sessao_id):

    sessao=Sessao.objects.get(id=sessao_id)
    
    context = {}

    if Pergunta.objects.filter(sessao=sessao).exists():
        pergunta = Pergunta.objects.get(sessao=sessao)
        
    else:
        pergunta = Pergunta.objects.create(sessao=sessao, texto_pergunta="Gosta de votar?", ativa=True)
        escolha_sim = Escolha.objects.create(pergunta=pergunta, texto_escolha="Sim")
        escolha_nao = Escolha.objects.create(pergunta=pergunta, texto_escolha="Não")

    if request.method == 'POST':
        if pergunta.ativa:
            pergunta.ativa = False
        else:
            pergunta.ativa = True
        pergunta.save()

    context['pergunta'] = pergunta

    # https://medium.com/geekculture/how-to-generate-a-qr-code-in-django-e32179d7fdf2
    factory = qrcode.image.svg.SvgImage    
    uri = request.build_absolute_uri(reverse('sondagem:votar', kwargs={'pergunta_id':pergunta.id}))
    img = qrcode.make(uri, image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream)
    context["svg"] = stream.getvalue().decode()

    return render(request, 'sondagem/pergunta.html', context)

def votar_view(request, pergunta_id):

    pergunta = Pergunta.objects.get(id=pergunta_id)

    if  pergunta.ativa and request.method == 'POST':
        escolha_id = request.POST['escolha']
        escolha = Escolha.objects.get(id=escolha_id)
        escolha.votos += 1
        escolha.save()

        return HttpResponseRedirect(reverse('sondagem:obrigado'))

    if  pergunta.ativa:
        context = {'pergunta': pergunta}
        return render(request, 'sondagem/votar.html', context)
    else:
        return HttpResponseRedirect(reverse('sondagem:obrigado'))

    
def obrigado_view(request):

    return render(request, 'sondagem/obrigado.html')



def resultados_view(request, pergunta_id):

    pergunta = Pergunta.objects.get(id=pergunta_id)

    escolhas = [escolha.texto_escolha for escolha in pergunta.escolha_set.all()]
    votos = [escolha.votos for escolha in pergunta.escolha_set.all()]

    plt.bar(escolhas, votos)
    plt.ylabel("votos")
    plt.autoscale()

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')


    buf.seek(0)
    string = base64.b64encode(buf.read())
    grafico = urllib.parse.quote(string)

    context = {'pergunta': pergunta, 'grafico':grafico}

    return render(request, 'sondagem/resultados.html', context)
