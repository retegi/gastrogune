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
        self.fields['text'].label = "Cuenta tu experiencia gastronómica / Zure esperientzia gastronomikoa partekatu"
        self.fields['complementNaturePlan'].widget.attrs.update({'class': 'form-control'})
        self.fields['complementNaturePlan'].label = "¿Qué plan relacionado con la NATURALEZA recomendarías para complementar la experiencia gastronómica? / NATURAREKIN lotuta dagoen zein plan osagarri gomendatuko zenuke?"
        self.fields['complementCulturePlan'].widget.attrs.update({'class': 'form-control'})
        self.fields['complementCulturePlan'].label = "¿Qué plan relacionado con la CULTURA recomendarías para complementar la experiencia gastronómica? / KULTURAREKIN lotuta dagoen zein plan osagarri gomendatuko zenuke?"
        self.fields['complementOtherPlan'].widget.attrs.update({'class': 'form-control'})
        self.fields['complementOtherPlan'].label = "¿Qué otra actividad recomendarías para complementar? / Zein beste plan osagarri gomendatuko zenuke"
        self.fields['qualityPrice'].widget.attrs.update({'class': 'form-control'})
        self.fields['qualityPrice'].label = "Calidad-Precio / Kalitatea-Prezioa"
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        self.fields['service'].label = "Servicio / Zerbitzua"
        self.fields['food'].widget.attrs.update({'class': 'form-control'})
        self.fields['food'].label = "Comida / Janaria"
        
        