from django import forms


class Item:
    id: int
    quantity: int

class OrderForm(forms.Form):
    table_number = forms.IntegerField(label='Table Number')
    dishes_with_quantity = [Item]