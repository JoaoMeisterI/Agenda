from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from contact import models
from contact.models import Contact

#O usuário ele valida
class RegisterForm(UserCreationForm):
    
    #Passando os Widgets
    
    first_name = forms.CharField(
        required=True,
        min_length=3,
        error_messages={
            'required': 'Nome inválido'
        }
        
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        error_messages={
            'required': 'Nome inválido'
        }
        
    )
    email = forms.EmailField()
    
    
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name','email','username','password1','password2',
        )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        #se User filtrado o objeto pelo email existir retorna um erro
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError("Já existe esse e-mail",code='invalid')
            )
            
        return email

class ContactForm(forms.ModelForm):
         
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        ),required=False
    ) 
         
    #Se Colocar  um nome diferente do models, cria um novo campo
  
    first_name = forms.CharField(
        widget=forms.TextInput(
             attrs={
            'placeholder': 'Escreva aqui',
            }
             
        ),
        help_text='Texto de Ajuda'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email','description','category','picture'
        )
        
        widgets = {
             'first_name': forms.TextInput(
                 attrs={
                     'placeholder': 'Escreva aqui',
                    
                 }
            
             ),
             'help_text': 'Ajuda para o User'
         }
       
        
    def clean(self):
        cleaned_data = self.cleaned_data
       
        print(cleaned_data)
        first_name = cleaned_data.get('first_name')
        print(first_name)
        last_name = self.cleaned_data.get('last_name')
        
        if first_name == last_name:
            
            msg= ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error("first_name",msg)
            self.add_error("last_name",msg)
            
        
        return super().clean()
    
    def clean_first_name(self):
        #Pegando os campos pelo cleaned_data
        first_name = self.cleaned_data.get('first_name')
        
        print(first_name)
        
        #Pode usar raise ou add_error
        
                
        if first_name == 'ABC':
            raise ValidationError(
                'Não digite ABC neste campo',
                code='invalid'
            )
        
        return first_name
    


class RegisterUpdateForm(forms.ModelForm):
 
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1