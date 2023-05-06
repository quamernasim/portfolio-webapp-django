from django import forms
from .models import BasicInfo, SocialMedia, Projects, Research, Education, Experience, Skills

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

class ProjectsForm(forms.ModelForm):
        
    class Meta:
        model = Projects
        fields = ['title', 'description', 'project_type', 'image', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'project_type': forms.Select(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
        }

class ResearchForm(forms.ModelForm):
            
    class Meta:
        model = Research
        fields = ['title', 'abstract', 'article_type', 'author_names', 'image', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'abstract': forms.Textarea(attrs={'class':'form-control'}),
            'article_type': forms.Select(attrs={'class':'form-control'}),
            'author_names': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
        }

class EducationForm(forms.ModelForm):
                    
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_year', 'end_year']
        widgets = {
            'institution': forms.TextInput(attrs={'class':'form-control'}),
            'degree': forms.TextInput(attrs={'class':'form-control'}),
            'start_year': forms.DateInput(attrs={'class':'form-control'}),
            'end_year': forms.DateInput(attrs={'class':'form-control'}),
        }