from django import forms
from ..models.basic import BasicInfo, SocialMedia

class BasicInfoForm(forms.ModelForm):

    class Meta:
        model = BasicInfo
        fields = ['firstname', 'lastname', 'email', 'country_code', 'phone_number', 'city', 'state', 'country', 'zip_code', 'address']
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'country_code': forms.NumberInput(attrs={'class':'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            'zip_code': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }

class SocialMediaForm(forms.ModelForm):
    
    class Meta:
        model = SocialMedia
        fields = ['facebook', 'twitter', 'instagram', 'linkedin', 'github', 'medium', 'stackoverflow', 'whatsapp', 'telegram']
        widgets = {
            'facebook': forms.URLInput(attrs={'class':'form-control'}),
            'twitter': forms.URLInput(attrs={'class':'form-control'}),
            'instagram': forms.URLInput(attrs={'class':'form-control'}),
            'linkedin': forms.URLInput(attrs={'class':'form-control'}),
            'github': forms.URLInput(attrs={'class':'form-control'}),
            'medium': forms.URLInput(attrs={'class':'form-control'}),
            'stackoverflow': forms.URLInput(attrs={'class':'form-control'}),
            'whatsapp': forms.URLInput(attrs={'class':'form-control'}),
            'telegram': forms.URLInput(attrs={'class':'form-control'}),
        }