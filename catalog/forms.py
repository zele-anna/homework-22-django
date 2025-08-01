from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms.fields import BooleanField

from catalog.models import Product

SPAM_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at', 'owner']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in SPAM_WORDS:
            if word in name.lower():
                raise ValidationError(f'В наименовании не может быть использовано слово {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for word in SPAM_WORDS:
            if word in description.lower():
                raise ValidationError(f'В описании не может быть использовано слово {word}')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена должна быть больше 0')
        return price
