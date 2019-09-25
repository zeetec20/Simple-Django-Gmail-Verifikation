from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from userSite.forms import FormLogin, FormRegister
from django.core.mail import send_mail
from userSite import token # for generate Token Activation or Url Activation
from users.models import CustomUser as User # CustomUser for create new user, 2 new field : token, activation

class Index(View):
    # print(dir(models))
    context = {}

    def get(self, request):
        return render(self.request, 'index.html', self.context)

class UserSite(View):
    mode = 0

    formLogin = FormLogin()
    formRegister = FormRegister()

    context = {
    }

    def login_user(self, request):
        if self.formLogin.is_valid():
            username_user = self.formLogin.cleaned_data['username']
            password_user = self.formLogin.cleaned_data['password']
            user = authenticate(request, username = username_user, password = password_user)
            print(user)
            if user is not None:
                login(self.request, user)
            else:
                return redirect('login')
        else:
            return redirect('login')

    def logout_user(self, request):
        if self.request.user.is_authenticated():
            logout(self.request)
        else:
            pass

    def register_user(self, request):
        if self.formRegister.is_valid():
            username_user = self.formRegister.cleaned_data['username']
            email_user = self.formRegister.cleaned_data['email']
            password_user = self.formRegister.cleaned_data['password']
            fullName_user = self.formRegister.cleaned_data['fullName']
            
            User.objects.create_user(username = username_user, password = password_user, email = email_user)

            getUser = User.objects.get(username = username_user)
            getUser.first_name = fullName_user
            getUser.is_active = False
            tokenUser = token.getToken(getUser.id, token.number2, token.number3, token.number4)
            activationUrl = token.getActivation(getUser.id, token.number2, token.number3, token.number4)
            getUser.token = tokenUser
            getUser.activation = activationUrl
            print(getUser.id)
            print(getUser)
            getUser.save()

            send_mail(
                'Subject',
                'Content',
                'youremail@gmail.com', #form
                [email_user], #to
                fail_silently=False,
            )

            return redirect('index')
        else:
            return redirect('index')

    def get(self, *args, **kwargs):
        self.template_name = 'index.html'

        if self.mode == 2:
            self.template_name = 'login.html'
            self.context['form'] = self.formLogin
        if self.mode == 1:
            self.template_name = 'register.html'
            self.context['form'] = self.formRegister
        if self.mode == 3:
            self.logout_user(self)
            return redirect('index')
        
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if self.mode == 2:
            self.formLogin = FormLogin(self.request.POST)
            self.login_user(self)
            return redirect('index')

        if self.mode == 1:
            self.formRegister = FormRegister(self.request.POST)
            self.register_user(self)
            return redirect('index')

class ActivationUser(View):
    
    template_name = 'activation.html'
    context = {}

    def get(self, request, *args, **kwargs):
        print(kwargs)
        getUser = User.objects.get(activation = kwargs['activationUrl'])
        self.context['account'] = getUser
        return render(self.request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        getUser = User.objects.get(activation = kwargs['activationUrl'])
        number1 = self.request.POST['number1']
        number2 = self.request.POST['number2']
        number3 = self.request.POST['number3']
        number4 = self.request.POST['number4']
        inputToken = "{} - {} - {} - {}".format(number1, number2, number3, number4)
        if getUser.token == inputToken:
            getUser.is_active = True
            getUser.save()
            return redirect('index')
