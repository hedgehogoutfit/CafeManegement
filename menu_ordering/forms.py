from django import forms
from django_select2.forms import Select2MultipleWidget

from menu_ordering.models import Order, Menu


class OrderForm(forms.ModelForm):
    order_items = forms.ModelMultipleChoiceField(queryset=Menu.objects.all(),
                                                 widget=forms.CheckboxSelectMultiple,
                                                 required=True)
    class Meta:
        model = Order
        fields = ['table_number', 'status', 'order_items']
