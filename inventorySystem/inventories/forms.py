from django.forms import ModelForm
from .models import Inventory


class InventoryUpdateForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "description", "note", "stock", "availability", "supplier"]


class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "description", "note", "stock", "availability", "supplier"]


