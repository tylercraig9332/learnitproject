from django.forms import ModelForm, TextInput

class ServerForm(ModelForm):

    class Meta:
        model = Server
        fields = ['username', 'password', 'email']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            }
