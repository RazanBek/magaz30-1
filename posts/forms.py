from django import forms


class ProductCreateForm(forms.Form):
    img = forms.ImageField(required=False)
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=8, decimal_places=2)


class CategoryCreateForm(forms.Form):
    name = forms.CharField(max_length=50)


class ReviewCreateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)