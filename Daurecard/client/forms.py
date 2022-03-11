from django import forms
from .models import Clients, Entreprise


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('nom', 'prenom','postnom', 'tel','entreprise', 'twitter', 'facebook', 'linkedin', 'profile')

        def __init__(self, *args, **kwargs):
            super(ClientForm, self).__init__(*args, **kwargs)
            self.fields['entreprise'].empty_label = "Selectionner entreprise"
            self.fields['profile'].required = False


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = "__all__"