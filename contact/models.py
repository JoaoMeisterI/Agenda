from django.db import models
from django.utils import timezone
#Para conseguir fazer um owner a gente importa direto um modulo de usuário
#Já cria a classe direto daí
from django.contrib.auth.models import User

# Create your models here.
# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

#Herança

#Criando uma nova classe para a inserção de uma foreign key

class Category(models.Model):
    class Meta:
        verbose_name = 'Category' #Singular
        verbose_name_plural = 'Categories' #Plural
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    #Por padrão são obrigatorios
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    #tipó do e-mail
    email = models.EmailField(max_length=254, blank=True) #Com o blanck você define se é obrigatório ou não, tem validação imbutida
    #Data é automática
    created_date = models.DateTimeField(default=timezone.now) #Função que pega a data atual
    #Tipo texto
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True) #Default coloca um falor automático, #Ele é de selecionar 
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m') #Dentro da pasta média ele vai criar uma pasta pictures / ano / mês
    
    
    #Criando chave estrangeira
    category = models.ForeignKey(
        #Esse on_delete define o que ocorre quando você exclui 
        # a categoria do contato, nesse caso ele vai ficar nulo
        Category, on_delete=models.SET_NULL,
        blank=True, null=True #Permito que esse campo seja nulo
    )
    
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        blank=True, null=True 
    )
    
    
    #ISSO DAQUI DIZ RESPEITO AO QUE VAI APARECER NA TELA DOS CONTATOS
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    
    