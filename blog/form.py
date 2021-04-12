from django.forms import ModelForm

from .models import Contact, Subscribe


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "content",)


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ("email",)
