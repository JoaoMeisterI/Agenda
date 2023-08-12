#Para redirecionar usa redirect
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id') #Se colocar [0:10] ele só pega os 10 primeiros contatos 
    #mesmo esquema do terminal
    #Isso vai ser um dict tu manipula igual um dict
    #Tem aquela questão do show que pode ser retirada alguma linha no adm, da´pi tu filtra por filtrer
    
    print(contacts.query) #Para analisar qual consulta está sendo feita
    
    #Dez contatos por pg
    paginator = Paginator(contacts,10)
    #Get passa valor a url ele não vai buscar
    page_number = request.GET.get("page")
    #É SEMELHANTE AO CONTACTS SÓ QUE LIMITADO, OBS AINDA ASSIM ESTÁ SEM
    page_obj = paginator.get_page(page_number)
    
    
    context = {
        'page_obj': page_obj,
        'site_title':'Contatos - Agenda',
    }
    
    return render(
        request,
        'contact/index.html',
        context
    )
    
    
def contact(request,contact_id):
    #Retorna um unico valor
    #Com o get e a pk ele vai puxar o Contact Object específico
    #Pode usar o filter nesse caso também
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    #Para só mostrar os contatos que estão com show=True
    single_contact = get_object_or_404(Contact,pk=contact_id, show=True)
    '''
        pode ser também
        
        single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id))
    
    '''
    # if single_contact is None:
    #     raise Http404
    
    site_title = f'{single_contact.first_name} {single_contact.last_name} - Agenda'
    
    
    context = {
        'contact': single_contact,
        'site_title': site_title,
        
        
    }
    
    return render(
        request,
        'contact/contact.html',
        context
    )
    

def search(request):
    #Puxa o name do input
    #Método de dicionário que pega algo, se não exisitr retorna vazio
    search_value = request.GET.get('q','').strip()
    
    if search_value == '':
        #Se for vazio redireciona para outra url
        return redirect("contact:index")
    
    #Pode passar quantos cambos quiser no icontains
    #Mas tem que usar o Q se ficar sem nada ele busca como campo iguais
    contacts = Contact.objects.all().filter(show=True).filter(Q(first_name__icontains =search_value)| Q(last_name__icontains =search_value)| Q(phone__icontains =search_value) |  Q(email__icontains =search_value)).order_by('-id') #Se colocar [0:10] ele só pega os 10 primeiros contatos 
    #mesmo esquema do terminal
    #Isso vai ser um dict tu manipula igual um dict
    #Tem aquela questão do show que pode ser retirada alguma linha no adm, da´pi tu filtra por filtrer
    
    print(contacts.query) #Para analisar qual consulta está sendo feita
    paginator = Paginator(contacts,10)
    #Get passa valor a url ele nnão vai buscar
    page_number = request.GET.get("page")
    #É SEMELHANTE AO CONTACTS SÓ QUE LIMITADO, OBS AINDA ASSIM ESTÁ SEM
    page_obj = paginator.get_page(page_number)
    
    
    context = {
        'page_obj': page_obj,
        'site_title':'Contatos - Agenda',
    }
    
    return render(
        request,
        'contact/index.html',
        context
    )