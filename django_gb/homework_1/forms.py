from django import forms


class GetProductClientDays(forms.Form):
    id_client = forms.IntegerField()
    days = forms.IntegerField()


class AddClientForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)
    email = forms.EmailField()
    phone_number = forms.IntegerField(min_value=80000000000, max_value=89999999999)
    address = forms.CharField(max_length=100)


class AddProductForm(forms.Form):
    product_name = forms.CharField(min_length=3, max_length=50)
    cost = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = forms.IntegerField()
    product_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Описание продукта'}))
    # product_image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "Изображение продукта"}))


class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Описание продукта"}))
    cost = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = forms.IntegerField()
    product_image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "Изображение продукта"}))


class ChoiceProductById(forms.Form):
    id_product = forms.IntegerField()
