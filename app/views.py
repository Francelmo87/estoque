from django.shortcuts import render



# @login_required(login_url='login')
def home(request):
    template_name= 'home.html'
    return render(request, template_name)