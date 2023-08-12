from django.contrib import admin
from contact import models
# Register your models here.
#Aqui tu coloca teu models para administrar

# Aqui vai ficar o model criado
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
#Ao fazer isso você coloca esse models para edição na pg admin
    #Esse list display coloca as informações como forma de tabela
    list_display = 'id','first_name', 'last_name', 'phone'
    #Ordendando a lista, se colocar um - na frente organiza de forma decrescente 
    ordering = 'id',
    #Colocando filtro
    # list_filter = ('created_date'),
    
    #PARA PESQUISAR CONTATOS
    
    search_fields = 'first_name', 'id', 'last_name', 'show',
    
    #Exibição de contatos por página
    
    list_per_page = 10 #Ou seja vai exibir um contato por página
    list_max_show_all = 200 #Isso impede que quando você aperte em mostrar todos que apareça mais que esse valor
    
    list_editable = 'first_name', #Permite a edição dos campos
    list_display_links = 'phone', #Permite que você entre no contato pelo número
    
    #Django tem seu próprio Shell
    #Query set são vários valores
    
    
#Registrando o outro models criado
@admin.register(models.Category)
#No caso linca com o foreign key da categoria criada
class CategoryAdmin(admin.ModelAdmin):
#Ao fazer isso você coloca esse models para edição na pg admin
    #Esse list display coloca as informações como forma de tabela
    list_display = 'name',
    #Ordendando a lista, se colocar um - na frente organiza de forma decrescente 
    ordering = 'id',
    #Colocando filtro
    # list_filter = ('created_date'),



