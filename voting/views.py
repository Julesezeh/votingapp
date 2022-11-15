import datetime
from re import X
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import *
from  .forms import Search

#The view function for question one
def index(request):
    if request.method == 'POST':
        #after form submission, this view function queries the AnnouncedPuResults Table with the inputed data and returns a page with the results
        form = Search(request.POST)
        if form.is_valid():
            #for debugging ..
            print("form valid")
            selected = form.cleaned_data.get('polling_unit')
            results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=selected)
            x = {'xo':results}
            return render(request,'results1.html',context=x)
        else:
            #for debugging
            print("NO")
    form = Search()
    valdict = {'form':form}
    return render(request,'index.html',context=valdict)

#The view function for question two
def page_two(request):
    if request.method == 'POST':
        lga_choice=request.POST.get('lga_id')
        if PollingUnit.objects.filter(lga_id=lga_choice):
            related_pollingunits = PollingUnit.objects.filter(lga_id=lga_choice)
            still= list(related_pollingunits)
            list2 = []
            for x in still:
                ling = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=x.polling_unit_id)
                ling = list(ling)

                if len(ling)>=1:
                    list2.append(ling)
            if len(list2)>0:
                final_results = list2[0]
            else:
                final_results = None
            mydict = {'results':final_results}
            return render(request,'results_two.html',context=mydict)
            
        else:
            pass

        return render(request,'results_two.html',context=None)
    
    lgas = Lga.objects.all()
    return render(request,'page_two.html',context={'x':lgas[1:],'pot':lgas[0]})

#The view function for question three
def page_three(request):
    if request.method == 'POST':
        pol_id=request.POST.get("pol-id")
        ent_user=request.POST.get('user')
        par=request.POST.get('party')
        score=request.POST.get('party-score')
        current_date = datetime.datetime.now()
        print(current_date)
        rex = AnnouncedPuResults(polling_unit_uniqueid=pol_id,party_abbreviation=par,party_score=score,entered_by_user=ent_user,date_entered=current_date,user_ip_address="192.168.1.101")
        rex.save()
        return render(request,'solution_three.html')

    parties = Party.objects.all()
    lgas = Lga.objects.all()
    return render(request,'page_three.html',context={'x':lgas[1:],'pot':lgas[0],'others':parties[1:],'potter':parties[0]})