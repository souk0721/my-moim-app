# coding: utf-8

from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core import validators

from but_moim.models import *
import datetime

class Moim_list_Form(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ('tel','user_name', )
        # exclude = ('filtered_image_file',)

class Moim_join_Form(forms.ModelForm):

    moim_name = forms.CharField(label=("모임이름"),
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '모임이름',
                                        'required' : 'true',

                                    })
                                )
    moim_deposit_date = forms.CharField(label=("입금날짜"),
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '입금날짜',
                                        'required' : 'true',

                                    })
                                )
    moim_account_name = forms.CharField(label=("계좌주인 이름"),
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '계좌주인 이름',
                                        'required' : 'true',

                                    })
                                )
    moim_account_bank = forms.CharField(label=("입금 은행명"),
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '입금 은행명',
                                        'required' : 'true',

                                    })
                                )
    moim_account_num = forms.CharField(label=("입금 계좌번호"),
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '입금 계좌번호',
                                        'required' : 'true',

                                    })
                                )
    moim_total_money = forms.IntegerField(label=("총 모임금액"),
                                widget=forms.NumberInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '총 모임금액',
                                        'required' : 'true',

                                    })
                                )

    deposit_amount = forms.IntegerField(label=('회비'),
                                widget=forms.NumberInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': '회비',
                                        'required' : 'true',

                                    })
                                )

    class Meta:
        model = moim_info
        exclude = ('user', 'moim_person_count','moim_total_money2','moim_symbol')

class MoimSearchForm(forms.Form):
    search_name = forms.CharField(label='검색',
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': '검색',
                                         'required': 'True',
                                     }
                                 )
                                 )


class SignupForm(UserCreationForm): #UserCreationForm의 models.form 을 상속 받는다.
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'True',
            }
        )
    )
    username = forms.RegexField(
        label="ID", max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and" " @/./+/-/_ only.",
        error_messages={
            'invalid': "This value may contain only letters, numbers and " "@/./+/-/_ characters."},
        widget=forms.TextInput
            (attrs={
            'class': 'form-control',
            'placeholder': 'ID',
            'required': 'true',
        }),
    )

    password1 = forms.CharField(label=("Password"),
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Password',
                                        'required' : 'true',

                                    })
                                )

    password2 = forms.CharField(label=("Password confirmation"),

                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Password confirmation',
                                        'required' : 'true',

                                    }),
                                help_text=("Enter the same password as above, for verification."))



    class Meta:
        model = User
        fields = ('username','email','password1','password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )


class User_Deposit(forms.ModelForm):

    class Meta:
        model = deposit_info
        fields = ('__all__')

        # widgets ={
        #     'deposit_date' : forms.DateInput(attrs={'class':'datepicker'}),

        # }

class User_Info2(forms.ModelForm):
    user_name = forms.CharField(label='이름',
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': '이름',
                                         'required': 'True',
                                     }
                                 )
                                 )

    tel = forms.CharField(label='전화번호',
                           required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': '전화번호',
                                   'required': 'True',
                               }
                           )
                           )

    class Meta:
        model = user_info
        fields = ('__all__')