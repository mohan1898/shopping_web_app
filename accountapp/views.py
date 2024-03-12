from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from accountapp import forms
from accountapp.models import Register

# def signup(request):
#     if request.method == "POST":
#         form = forms.registerform(request.POST)
#         if form.is_valid():
#             password = form.cleaned_data.get('password')
#             confirm_password = form.cleaned_data.get('confirm_password')
#             if password != confirm_password:
#                 messages.error(request, "Passwords do not match.")
#                 return render(request, 'accounts/signup.html', {'form': form})
#             # Additional password validations can be added here if needed
#             form.save(commit=True)
#             messages.success(request, "Your account has been created successfully!")
#             return HttpResponseRedirect('/accounts/login/')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = forms.registerform()

#     return render(request, 'accounts/signup.html', {'form': form})


# def register(request):   
#     return render(request,'accounts/user.html')


# def loginUser(request):
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             # Authenticate user using email as username
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 # Redirect to the dashboard or any other desired page
#                 # return redirect('/user_dash')  # Update 'dashboard' with your actual URL name
#                 return HttpResponseRedirect('/user_dash')
#             else:
#                 form.add_error(None, "Invalid email or password.")
#     else:
#         form = forms.LoginForm()

#     return render(request, 'accounts/login.html', {'form': form})
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')

def loginUser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/dashboard/')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email , password)
        user =  authenticate(username=email , password=password)
        if user is not None:
            messages.info(request, "Invalid Password")
            login(request , user)
            return HttpResponseRedirect('/accounts/dashboard/')
       
    return render(request , 'accounts/login.html')



def dashboard(request):   
    name = request.user
    return render(request,'accounts/user_dash.html' , {'name':name})



def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)
        if user.exists():
            messages.info(request, "User Already Exists Please Login")
            return HttpResponseRedirect('/accounts/login')
        else:
            user = User.objects.create_user(first_name=username,username=username, email=email)
            user.set_password(password)
            user.save()
            messages.info(request, "Account created Successfully!")
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'accounts/signup.html')