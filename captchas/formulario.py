from django import forms

class formularioCaptcha(forms.Form):
    valor_Captcha=forms.CharField(max_length=5)
    codigo_Unidad=forms.IntegerField()
    numero_Expediente=forms.IntegerField()
