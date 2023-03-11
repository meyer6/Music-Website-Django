from django.shortcuts import render
from django.http import HttpResponse
from .forms import UsersForm
from .models import Users
from django.http import HttpResponseRedirect
import re
from datetime import datetime as time

def Valid_details(email2,password,date):
    try:
        users = Users.objects.get(email = email2)
        return "Email already registered"
    except:
        a=1
    if len(password)<8 :
        return "Password must be more than 8 characters"
    if bool(re.match(r'\w*[A-Z]\w*', password)) == False:
        return "Password must have upper case letters"
    if bool(re.match(r'\w*[a-z]\w*', password)) == False:
        return "Password must have lower case letters"        
    if any(char.isdigit() for char in password) == False:
        return "Password must have numbers"
    if int(date.replace("-","")) >= int(str(time.today().strftime('%Y-%m-%d')).replace("-","")):
        return "Please input valid date"
    return True

user1 = []

def login(request):
    global user1
    if request.method == 'POST':
        users = Users.objects.all()
        for user in users:
            if user.email == request.POST.get("email", "0") and user.password == request.POST.get("password", "0"):
                user1 = [user.email, user.password, user.date.strftime('%Y-%m-%d'), user.fav_artist, user.fav_genre]
                return HttpResponseRedirect('/main/')

    return render(request, "Login.html", { 'name': 'Mosh'})

def add_user(request):
    global user1
    issue = ""
    if request.method == 'POST':  # data sent by user
        print(request.POST)
        form = UsersForm(request.POST)
        if form.is_valid():
            if Valid_details(request.POST.get("email", "0"), request.POST.get("password", "0"), request.POST.get("date", "0")) == True:
                form.save()  # this will save Car info to database
                user1 = [request.POST.get("email", "0"), request.POST.get("password", "0"), request.POST.get("date", "0"), request.POST.get("fav_artist", "0"), request.POST.get("fav_genre", "0")]
                return HttpResponseRedirect('/main/')
            issue = Valid_details(request.POST.get("email", "0"), request.POST.get("password", "0"), request.POST.get("date", "0"))

    return render(request, 'Create.html', {'issue': issue})