from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import ClientForm, EntrepriseForm

from .models import Clients, Entreprise

# Create your views here.

#Client CRUD
def client_list(request):
    clients = Clients.objects.all()
    return render(request, 'client/clients.html', {'clients': clients})

def details_client(request, id):
    try:
        client = Clients.objects.get(id=id)
    except Clients.DoesNotExist:
        client = None
    return render(request, 'client/details_client.html', {'client': client})



def creer_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            nom = form.cleaned_data.get("nom")
            prenom = form.cleaned_data.get("prenom")
            postnom = form.cleaned_data.get("postnom")
            tel = form.cleaned_data.get("tel")
            entreprise = form.cleaned_data.get("entreprise")
            twitter = form.cleaned_data.get("twitter")
            facebook = form.cleaned_data.get("facebook")
            linkedin = form.cleaned_data.get("linkedin")
            profile = form.cleaned_data.get("profile") 
            form = Clients.objects.create( 
                                 nom = nom,
                                 prenom = prenom,
                                 postnom = postnom,
                                 tel = tel,
                                 entreprise = entreprise,
                                 twitter = twitter,
                                 facebook = facebook,
                                 linkedin = linkedin,
                                 profile = profile,
                                 ) 
            form.save()
            return redirect('client')
    else:
        form = ClientForm()
    return render(request, 'client/creer_client.html', {'form': form})


def modifier_client(request, id):
    client = Clients.objects.get(id=id)
    if client:
        if request.method == 'POST':
            if client:
                form = ClientForm(request.POST, request.FILES, instance=client)
                if form.is_valid():
                     nom = form.cleaned_data.get("nom")
                     prenom = form.cleaned_data.get("prenom")
                     postnom = form.cleaned_data.get("postnom")
                     tel = form.cleaned_data.get("tel")
                     entreprise = form.cleaned_data.get("entreprise")
                     twitter = form.cleaned_data.get("twitter")
                     facebook = form.cleaned_data.get("facebook")
                     linkedin = form.cleaned_data.get("linkedin")
                     profile = form.cleaned_data.get("profile") 
                     form = Clients.objects.create( 
                                            nom = nom,
                                            prenom = prenom,
                                            postnom = postnom,
                                            tel = tel,
                                            entreprise = entreprise,
                                            twitter = twitter,
                                            facebook = facebook,
                                            linkedin = linkedin,
                                            profile = profile,
                                            ) 
                form.save()
                return redirect('client')
        
        else:
            form = ClientForm(instance=client)
    return render(request, 'client/modifier_client.html', {'form': form})

def supprimer_client(request, id):
    client = Clients.objects.get(id=id)
    if client:
        if request.method == 'POST':
            client.delete()
            return redirect("client_list")
    return render(request, 'client/supprimer_client.html', {'client':client})



#Entreprise CRUD
def entreprise_list(request):
    entreprises = Entreprise.objects.all()
    return render(request, 'entreprise/entreprises', {'entreprises': entreprises})

def creer_entreprise(request):
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entreprise_list')
    else:
        form = ClientForm()
    return render(request, 'entreprise/creer_entreprise.html', {'form': form})


def modifier_entreprise(request, id):
    entreprise = Entreprise.objects.get(id=id)
    if entreprise:
        if request.method == 'POST':
            if entreprise:
                form = EntrepriseForm(request.POST, instance=entreprise)
                if form.is_valid():
                    form.save()
                    return redirect('entreprise_list')
        
        else:
            form = EntrepriseForm(instance=entreprise)
    return render(request, 'entreprise/modifier_entreprise.html', {'form': form})

def supprimer_entreprise(request, id):
    entreprise = Entreprise.objects.get(id=id)
    if entreprise:
        if request.method == 'POST':
            entreprise.delete()
            return redirect('entreprise_list')

