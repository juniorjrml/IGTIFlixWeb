from django.db.models import QuerySet
from django.shortcuts import render
from . import forms
from . import models
from genero import models as modeloGenero


def cadastro(request):
    form = forms.SerieForm()
    if request.method == 'POST':
        form = forms.SerieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

        else:
            print("formulário não é válido")
    serie_list = models.Serie.objects.order_by('name')
    data_dict = {'form': form, 'serie_records': serie_list}
    return render(request, 'serie/serie.html', data_dict)


def delete(request, id):
    print("delete")
    models.Serie.objects.filter(id=id).delete()
    form = forms.SerieForm()
    serie_list = models.Serie.objects.order_by('name')
    data_dict = {"serie_records": serie_list, 'form': form}
    return render(request, 'serie/serie.html', data_dict)


def update(request, id):
    item = models.Serie.objects.get(id=id)
    if request.method == "GET":
        form = forms.SerieForm(initial={'name': item.name, 'Genero':item.Genero})
        data_dict = {'form': form}
        return render(request, 'serie/serie_upd.html', data_dict)
    else:
        form = forms.SerieForm(request.POST)
        item.name = form.data['name']
        item.Genero = modeloGenero.Genero.objects.filter(id=form.data['Genero'])[0]
        #objects.filter(id=form.data['idGenero'])
        #print(type(modeloGenero.Genero.objects.filter(id=form.data['idGenero'])[0]))
        item.save()
        serie_list = models.Serie.objects.order_by('name')
        data_dict = {"serie_records": serie_list, 'form': form}
        return render(request, 'serie/serie.html', data_dict)