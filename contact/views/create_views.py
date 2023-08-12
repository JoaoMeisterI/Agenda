#Para redirecionar usa redirect
from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import Http404
from django.core.paginator import Paginator
#Para criar formulários importa o seu Models e o django forms
from django.core.exceptions import  ValidationError
from contact.Forms import ContactForm
#Para pegar contato para atualizar vamos tem que importar
from django.urls import reverse
#Importa esses dois para conseguir usar a instance
from contact.models import Contact
from contact.Forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def create(request):
    #Como ele já está logado eu consigo pegar o usuário por request.user e colocar ele como owner do contato
   
   #Passando a variavel para  a action do form
   
    form_action = reverse('contact:create')
    
   
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
      
        context = {
            #Para passar os dados
            'form': form,
            'form_action': form_action,
        }
       
        
        #Verificando se um formaulário é valido
        if form.is_valid():
            print("Formulário é valido")
            #commit false não salva
            # contact = form.save(commit=False)
            # contact.show = False
            # contact.save()
            #Para salvar coloca o nome do model.save
            ##Não vou salvar o contato ainda
            contact = form.save(commit=False)
            ##Mas eu tenho o contato
            #Salvando o owner no campo owner
            contact.owner = request.user
            
            contact.save()
            print(contact.owner)
            #Para atualizar a página você usa um redirect
            #URL + PARÂMETRO
            return redirect('contact:update',contact_id=contact.pk)
            
            
        
       
        return render(
            request,
            'contact/create.html',
            context
        )
    
    
    context = {
        'form': ContactForm(),
        'form_action': form_action
    }
        
    return render(
        request,
        'contact/create.html',
        context
    )
    
#Ele salva e já manda para o update

@login_required(login_url='contact:login')
def update(request,contact_id):
    
    #Instance é para criar os dados do formulário mas atrelado a uma instância que já existe
   
   #Passando a variavel para  a action do form
   
   #Só vai deixar atualizar se for o owner, pois estamos passando o owner como parâmetro
    contact = get_object_or_404(Contact,pk=contact_id, show=True, owner=request.user)
    form_action = reverse('contact:update',args=(contact_id,))
   
   
    if request.method == 'POST':
        #Passa a instancia como parâmetro isso vai indicar que o obejto já existe e é só para atualizar
        form = ContactForm(request.POST,  request.FILES, instance=contact)
      
        context = {
            #Para passar os dados
            'form': form,
            'form_action': form_action,
        }
       
        #Verificando se um formaulário é valido
        if form.is_valid():
            print("Formulário é valido")
            #commit false não salva
            # contact = form.save(commit=False)
            # contact.show = False
            # contact.save()
            #Para salvar coloca o nome do model.save
            contact = form.save()
            #Para atualizar a página você usa um redirect
            #URL + PARÂMETRO
            return redirect('contact:update',contact_id=contact.pk)
            
       
       
        return render(
            request,
            'contact/create.html',
            context
        )
    

    context = {
        'form': ContactForm(instance=contact)
    }
        
    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def delete(request,contact_id):
    contact = get_object_or_404(
        Contact,pk=contact_id, show=True,owner=request.user
    )
    #Excluindo o contato
    #Por padrão passa "no"
    confirmation = request.POST.get("confirmation","no")
   
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(request,
                'contact/contact.html',
                {
                  'contact': contact,
                  'confirmation': confirmation,    
                }
            )