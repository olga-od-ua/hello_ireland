""" A Module for customising forms related to a Product """
from django import forms
from django.forms import ModelForm
from .models import Product, Category, ProductReview
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """ A Class to generate the Product form """
    class Meta:
        """ A Meta Class to customize the Product form rendering """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 product-mngmt-field'


class ProductReviewForm(forms.ModelForm):
    """ A Class to generate the Product Review form """
    class Meta:
        """ A Class to customize the Product Review form rendering """
        model = ProductReview
        fields = ('rating', 'review_message',)

        RATING_CHOICES = (
                ('', 'Please rate the product where 1 is the'
                 'lowest and 5 is the highest'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5'),
                )

        widgets = {
            'review_message': forms.Textarea(attrs={
                'class': 'form-control',
                'maxlength': '200',
                }),
            'rating': forms.Select(choices=RATING_CHOICES, attrs={
                'class': 'form-control',
                'required': True}),
        }
        labels = {
            'review_message': 'Please leave your review here:',
        }
