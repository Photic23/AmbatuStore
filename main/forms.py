from django.forms import ModelForm
from main.models import item


class ItemForm(ModelForm):
    class Meta:
        model = item
        fields = ["name", "amount", "description", "image"]

