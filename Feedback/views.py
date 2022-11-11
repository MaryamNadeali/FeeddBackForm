from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import MulQuestion, TxtQuestion, MultipleAnswer, Answer, TxtAnswer
from .forms import BooleanForm, TextForm, RegisterForm, LoginForm

# Create your views here.
class RegisterView(View):
    
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'account/register.html', {'register_form':register_form})
    
    def post(self, request):
        register_form = RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password('password')
                user.save()
                messages.success(request,'ثبت اطلاعات با موفقیت انجام شد')
                return redirect('Feedback:login')
            else:
                messages.error(request, 'اطلاعات وارد شده معتبر نمی باشد')
                return render(request, 'account/register.html', {'register_form': register_form})
            
class LoginView(View):
    
    def get(self,request, *args, **kwargs):
        login_form = LoginForm()
        return render(request,'account/login.html', {'login_form':login_form})
    
    def post(self, request):
        login_form = LoginForm()
        username = request.POST['username']
        print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',username)
        password = request.POST['password']
        print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',password)
        user = authenticate(request, username=username, password=password)
        print('PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP',user)
        if user is not None:
            
            login(request, user)
            return redirect('Feedback:feedbackform')
        else:
            messages.warning(request,'کاربر با این مشخصات یافت نشد')
            return render(request, 'account/login.html', {'login_form':login_form})
                    
    
class FeedbackFormView(View):
    
    def get(self, request):

        mul_que = MulQuestion.objects.all()
        multiple_anses = MultipleAnswer.objects.all()
        context = {
            'mul_que' : mul_que,
            'multiple_anses' : multiple_anses,
            }
        print(context)
        return render(request, 'question/que.html', context)
    
    def post(self, request, *args, **kwargs):
        questions = MulQuestion.objects.all()
        multiple_anses = MultipleAnswer.objects.all()
        for question in questions:
            print('question',question)
            if question.type == 'multianswer':
                form = BooleanForm()
                if request.method == 'POST': 
                    form = BooleanForm(request.POST)
                    print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
                    multiple_anses = MultipleAnswer.objects.all().filter(que=question)
                    print('aaaaaaaaaaaaaaaaaaaaaa',multiple_anses)
                    for i in range(0,len(multiple_anses)):
                        print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',request.POST)
                        if form.is_valid():
                            print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
                            bool_ans = form.cleaned_data.get('bool_ans')
                            print('fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',bool_ans)
                            answer = Answer.objects.create(que=question,ans=multiple_anses[i],bool_ans=bool_ans) 
                            answer.save() 
            else:
                txt_form = TextForm()
                if request.method == 'POST':
                    txt_form = TextForm(request.POST)
                    print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',request.POST)
                    if txt_form.is_valid():
                        txt_ans = txt_form.cleaned_data.get('txt_ans')
                        print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr',txt_ans)
                        answer = TxtAnswer.objects.create(que=question,txt_ans=txt_ans)
                        answer.save()
        return render(request, 'question/end.html') 
            
        # else:
        #     return render(request, 'question/que.html')           
                
                    
        
