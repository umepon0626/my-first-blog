from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100)
    message = forms.CharField(label='お問い合わせ内容', max_length=1000)
    sender = forms.CharField(label='お名前')
