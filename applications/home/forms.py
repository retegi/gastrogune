from django import forms
from django.forms import ModelForm, Textarea
from .models import Comment

"""class Comment_form(ModelForm):
    class Meta:
        model = Comment
        fields = ['text','complementNaturePlan','complementCulturePlan','complementOtherPlan','qualityPrice','service','food']
        widgets = {
            'text': Textarea(attrs={'class':'col-12', 'rows': 5,}),
            'complementOtherPlan': Textarea(attrs={'class':'col-12', 'rows': 5}),
            'complementNaturePlan': Textarea(attrs={'class':'col-12', 'rows': 5}),
            'complementCulturePlan': Textarea(attrs={'class':'col-12', 'rows': 5}),
           
        }"""

class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','complementNaturePlan','complementCulturePlan','complementOtherPlan','qualityPrice','service','food')

    def __init__(self,*args, **kwargs):
        super(Comment_form, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].label = "Comentario"
        self.fields['complementNaturePlan'].widget.attrs.update({'class': 'form-control'})
        self.fields['complementNaturePlan'].label = "Plan con Naturaleza"
        self.fields['complementCulturePlan'].widget.attrs.update({'class': 'form-control'})
        self.fields['complementCulturePlan'].label = "Plan con Cultura"
        self.fields['complementOtherPlan'].widget.attrs.update({'class': 'form-control'})
        self.fields['complementOtherPlan'].label = "Otros planes"
        self.fields['qualityPrice'].widget.attrs.update({'class': 'form-control'})
        self.fields['qualityPrice'].label = "Calidad-Precio"
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        self.fields['service'].label = "Servicio"
        self.fields['food'].widget.attrs.update({'class': 'form-control'})
        self.fields['food'].label = "Comida"
        
        