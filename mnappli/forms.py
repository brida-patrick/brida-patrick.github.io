from typing import Any
from django import forms

from .models import Book , Author



class BookModel(forms.ModelForm):
    Author = forms.ModelChoiceField(label="Auteur", queryset= Author.objects.all())



    class Meta:
        model= Book
        fields= ["title","quantity","Author"]
        labes= {"title":"titre","quantity":"quantite"}

    #def clean_quantity(self):
        #quantity= self.cleaned_data['quantity']

        #if quantity <= 0 or quantity > 100:
           # raise forms.ValidationError("la quantite doit etre 0<quantie>100")
        
        
        #return quantity
    

    def clean(self):
        title= self.cleaned_data.get("title")
        quantity= self.cleaned_data.get("quantity")

        if title and quantity:
            if title.startswith("la") and quantity > 25:
                raise forms.ValidationError("impossi d'ajouter ce livre")
        return self.cleaned_data
      


