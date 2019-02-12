from django import forms

pl = 'Vincius querido, gostaria de te apresentar o Banden Powell compositor e violonista excepcional! Suas músicas tem embalado os bares do rio. Badinho o Vinicius é um poeta singular e pode criar belas letras para suas composições'

class IntroduceForm(forms.Form):
    from_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Tom Jobim'}))
    from_email = forms.EmailField(label='',
                                widget=forms.EmailInput(attrs={'placeholder': 'tom.jobim@mpb.br'}))

    person1_name = forms.CharField(label='',
                                    widget=forms.TextInput(attrs={'placeholder': 'Vinicius de Moraes'}))

    person1_email = forms.EmailField(label='',
                                      widget=forms.EmailInput(attrs={'placeholder': 'vinicius.moraes@mpb.br'}))

    person2_name = forms.CharField(label='',
                                    widget=forms.TextInput(attrs={'placeholder': 'Baden Powell'}))
    person2_email = forms.EmailField(label='',
                                      widget=forms.EmailInput(attrs={'placeholder': 'baden.powell@mpb.br'}))

    message = forms.CharField(label='', widget= forms.Textarea
                (attrs={'placeholder': pl, 'rows': '5'}))
