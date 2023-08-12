from django.shortcuts import render, redirect
from contact.Forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
#tem um decorator para fazer com que o usuário acesse a view só se ele
#estiver logado
from django.contrib.auth.decorators import login_required


def register(request):
    
    
    
    form = RegisterForm()
    
    #Colocando uma mensagem
    
   
    #Você precisa capturar ela em algum lugar
    
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    

        if form.is_valid():
            form.save()
            messages.success(request,'Usuário cadastrado com sucesso')
            return redirect("contact:login")

        
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
        
    )    
    
    #Bp0RbXbNO8pwQAQ
    
    

def login_view(request):
     
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            #Logando o usuário
            auth.login(request,user)
            messages.success(request,"Logado com Sucesso")
            return redirect('contact:index')
        messages.error(request,'login inválido')
    
    
    return render(
    request,
    'contact/login.html',     
    {
        'form': form     
    }
    
    )
     
#Isso obriga o usuário estar logado caso contrário ele manda para a login novamente
@login_required(login_url='contact:login')
def user_update(request):
    
    #Para identificar que você está logado com esse usuário 
    form = RegisterUpdateForm(instance=request.user)
    
    # Se não for post eu renderizo o formulário
    if request.method != 'POST':
    
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )     
     
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
     
    if not form.is_valid():
        return render(
        request,
        'contact/user_update.html',
        {
            'form': form
        }
    )     
        
    form.save()
    
    return redirect('contact:login')
         
#Atualiza 
@login_required(login_url='contact:login')     
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')