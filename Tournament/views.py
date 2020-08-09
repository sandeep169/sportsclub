from django.shortcuts import render, redirect
from .models import TableTennis,Badminton,Chess,Cricket
from .forms import  AddTournament , Participate
# AddTableTennis,AddTournament,AddChess,AddCricket

#function name should not be same with your module name defined in module.py
#it will generate error   objs = imgs.objects.all()
#AttributeError: 'function' object has no attribute 'objects'

def Tournament(request):
    return render(request, 'tournament.html')

def TournamentIndex(request):
    return redirect("/tournament")

def home(request):
    return redirect("/")


def TableTennisFn(request):
    obj = TableTennis.objects.all()
    return render(request, 'tournament.html', {'obj': obj})

def ChessFn(request):
    obj = Chess.objects.all()
    return render(request, 'tournament.html', {'obj': obj})

def BadmintonFn(request):
    obj = Badminton.objects.all()
    return render(request, 'tournament.html', {'obj': obj})

def CricketFn(request):
    obj = Cricket.objects.all()
    return render(request, 'tournament.html', {'obj': obj})


def addTour(request):
    return render(request,'organiseEvents.html')

def addBadmintion(request):
    form = AddTournament()
    if request.method == 'POST':

        form = AddTournament(request.POST,request.FILES)
        if form.is_valid():

            name = form.cleaned_data.get("tour_name")
            venues = form.cleaned_data.get("venue")
            date = form.cleaned_data.get("tour_start_date")
            reg_date = form.cleaned_data.get("reg_close_date")
            org = form.cleaned_data.get("organiser_name")
            prizes = form.cleaned_data.get("prize")
            desc = form.cleaned_data.get("description")
            total_teams = form.cleaned_data.get("total_team")
            img = form.cleaned_data.get("tour_img")
            p = Badminton.objects.create(tour_name=name, venue=venues,tour_start_date=date ,reg_close_date=reg_date,
                                         organiser_name=org,prize=prizes, description=desc, total_team=total_teams,
                                         tour_img=img)
            p.save()
            print("data submitted")
            return redirect('/tournament/badminton')

    return render(request,'addTournament.html',{'form':form})

def addCricket(request):
    form = AddTournament()

    if request.method == 'POST':
        form = AddTournament(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("tour_name")
            venues = form.cleaned_data.get("venue")
            date = form.cleaned_data.get("tour_start_date")
            reg_date = form.cleaned_data.get("reg_close_date")
            org = form.cleaned_data.get("organiser_name")
            prizes = form.cleaned_data.get("prize")
            desc = form.cleaned_data.get("description")
            total_teams = form.cleaned_data.get("total_team")
            img = form.cleaned_data.get("tour_img")
            p = Cricket.objects.create(tour_name=name, venue=venues, tour_start_date=date, reg_close_date=reg_date,
                                         organiser_name=org, prize=prizes, description=desc, total_team=total_teams,
                                         tour_img=img)
            p.save()
            return redirect('/tournament/cricket')

    return render(request, 'addTournament.html', {'form': form})

    
def addChess(request):
    form = AddTournament()
    if request.method == 'POST':
        form = AddTournament(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("tour_name")
            venues = form.cleaned_data.get("venue")
            date = form.cleaned_data.get("tour_start_date")
            reg_date = form.cleaned_data.get("reg_close_date")
            org = form.cleaned_data.get("organiser_name")
            prizes = form.cleaned_data.get("prize")
            desc = form.cleaned_data.get("description")
            total_teams = form.cleaned_data.get("total_team")
            img = form.cleaned_data.get("tour_img")
            p = Chess.objects.create(tour_name=name, venue=venues, tour_start_date=date, reg_close_date=reg_date,
                                         organiser_name=org, prize=prizes, description=desc, total_team=total_teams,
                                         tour_img=img)
            p.save()

            return redirect('/tournament/chess')

    return render(request, 'addTournament.html', {'form': form})

def addTT(request):
    form = AddTournament()
    if request.method == 'POST':

        form = AddTournament(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("tour_name")
            venues = form.cleaned_data.get("venue")
            date = form.cleaned_data.get("tour_start_date")
            reg_date = form.cleaned_data.get("reg_close_date")
            org = form.cleaned_data.get("organiser_name")
            prizes = form.cleaned_data.get("prize")
            desc = form.cleaned_data.get("description")
            total_teams = form.cleaned_data.get("total_team")
            img = form.cleaned_data.get("tour_img")
            p = TableTennis.objects.create(tour_name=name, venue=venues, tour_start_date=date, reg_close_date=reg_date,
                                         organiser_name=org, prize=prizes, description=desc, total_team=total_teams,
                                         tour_img=img)
            p.save()
            print("data submitted")
            return redirect('/tournament/tt')

    return render(request, 'addTournament.html', {'form': form})

def participate(request):
    part = Participate()

    return render(request,'participate.html',{'part':part})

def delete(request):
    pass

def update(request):
    pass

