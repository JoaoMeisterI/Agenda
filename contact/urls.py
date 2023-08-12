from django.urls import path
from contact import views

#esse app name é o primeiro que coloca na url dinâmica, só usa quadno é dinâmica
app_name  = 'contact'

urlpatterns = [
    
    #CONTACT
    
    #Quanto mais descriçaõ ela tem vai passando a url para cima
    #Sempre colocar uma barra final ao lado da url
    #Para criar contato ou deletar contato a pessoa vai ter que estar logada e aquele contato vai ter que ser dela
    path('contact/<int:contact_id>/',views.contact, name='contact'),
    path('contact/<int:contact_id>/update',views.update, name='update'),
    path('contact/<int:contact_id>/delete',views.delete, name='delete'),
    path('contact/create/',views.create, name='create'),
    path('search/',views.search, name='search'),
    path('',views.index, name='index'),
    #Pedindo um parâmetro dinâmico
   
    #USER
    path('user/create/',views.register, name='register'),
    path('user/login/',views.login_view, name='login'),
    path('user/logout/',views.logout_view, name='logout'),
    path('user/update/',views.user_update, name='user_update'),

]
