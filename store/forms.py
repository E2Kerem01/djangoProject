from django import forms
from .models import QuickAdd, Category


"""class QuickProductForm(forms.ModelForm):
    class Meta:
        model = QuickProduct
        fields = '__all__'"""


class QuickAddForm(forms.ModelForm):
    class Meta:
        model = QuickAdd
        fields='__all__'

        CURRENCY_CHOICES = [
            ('USD', 'Dolar'),
            ('EUR', 'Euro'),
            ('TRY', 'Türk Lirası'),
            # Diğer para birimleri buraya eklenebilir
        ]

        category = forms.ModelChoiceField(queryset=Category.objects.all())
        currency = forms.ChoiceField(choices=CURRENCY_CHOICES)