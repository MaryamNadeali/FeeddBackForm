from dataclasses import fields
from socket import fromshare
from tabnanny import verbose
from xmlrpc.client import boolean
from django import forms
from django.contrib.auth.models import User
from .models import MulQuestion, TxtQuestion, MultipleAnswer, TxtAnswer, Answer

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        
class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields=['username', 'password']

class BooleanForm(forms.ModelForm):
    # bool_ans = forms.BooleanField()
    # txt_ans =  forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Answer
        fields = ['bool_ans']
        
class TextForm(forms.ModelForm):
    class Meta:
        model = TxtAnswer
        fields = ['txt_ans']
    
    # def save(self, *args, **kwargs):
    #     print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    #     questions = MulQuestion.objects.all()
    #     multiple_anses = MultipleAnswer.objects.all()
    #     for question in questions:
    #         if question.type == 'multianswer':
    #             print('question',question)
    #             multiple_anses = MultipleAnswer.objects.all().filter(que=question)
    #             print('aaaaaaaaaaaaaaaaaaaaaa',multiple_anses)
    #             for i in range(0,len(multiple_anses)):
                    
    #                     data = self.cleaned_data
    #                     answer = Answer.objects.create(que=self.question,ans=self.multiple_anses[i],bool_ans=data['bool_ans'])
    #                     # answer.save()
    #         else:
    #             data = self.cleaned_data
    #             answer = Answer.objects.create(que=self.question,txt_ans=data['txt_ans'])
    #             # answer.save()
                

                
            
            
    
    
                
            
            

    