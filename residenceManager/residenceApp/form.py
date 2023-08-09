from django import forms
from .models import StudentModel, User, PaymentModel

class StudentForm(forms.ModelForm):
    

    student_number = forms.CharField(label="Numéro Etudiant", max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Veuillez entrer votre Numéro Etudiant', 'name': 'student_number'}))
    telephone = forms.CharField(label="Téléphone", max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Veuillez entrer votre Numéro Téléphone', 'name': 'telephone'}))
    department = forms.CharField(label="Département", max_length=255)
    
    
    class Meta:
        model = StudentModel
        fields = ("student_number", "telephone", "department")

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="Prénom", max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Veuillez entrer votre Prénom', 'name': 'first_name'}))
    last_name = forms.CharField(label="Nom", max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Veuillez entrer votre Nom', 'name': 'last_name'}))
    email = forms.CharField(label="Email", max_length=255, widget=forms.EmailInput(attrs={'placeholder': 'Veuillez entrer votre Email', 'name': 'email'}))
    password = forms.CharField(label="Mot de passe", max_length=255, widget=forms.PasswordInput(attrs={'placeholder': 'Veuillez entrer votre Mot de passe', 'name': 'password'}))
    password2 = forms.CharField(label="Confirmation mdp", max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Veuillez confirmer le mot de passe', 'name': 'password2'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password2')


class PaymentForm(forms.ModelForm):
    amount = forms.FloatField(label="Montant", widget=forms.TextInput(attrs={'placeholder': 'Veuillez entrer le montant du paiement', 'name': 'amount'}))
    mounth = forms.ChoiceField(label="Mois", choices=PaymentModel.MOUNTH_CHOICE, widget=forms.Select(attrs={'placeholder': 'Veuillez sélectionner le mois', 'name': 'mounth'}))
    payment_status = forms.BooleanField(label='Statut de paiement', widget=forms.CheckboxInput(attrs={"name": "payment_status"}))


    class Meta:
        model = PaymentModel
        fields = ("amount", "mounth", "payment_statut")