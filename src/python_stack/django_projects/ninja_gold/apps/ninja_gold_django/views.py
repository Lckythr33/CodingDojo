from django.shortcuts import render, redirect
import random

def homepage(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'activities' in request.session:
        request.session['activities'] = []
    print("in the homepage function") 
    return render(request,'index.html') 

def process_money(request):
    print("came in the process money method")
    if request.POST['building'] == "farm":
        gold_to_add = random.randint(10,20)
        message = f"Earned {gold_to_add} from the Farm!"
    if request.POST['building'] == "cave":
        gold_to_add = random.randint(5,10)
        message = f"Earned {gold_to_add} from the Cave!"
    if request.POST['building'] == "house":
        gold_to_add = random.randint(2,5)
        message = f"Earned {gold_to_add} from the House!"
    if request.POST['building'] == "casino":
        gold_to_add = random.randint(-50,50)
        message = f"Earned {gold_to_add} from the Casino!"

        if gold_to_add > 0:
            message = f"Earned {gold_to_add} from {request.POST['building']}!"
        else:
            message = f"Lost {-gold_to_add} from the Casino!"

    request.session['activities'].insert(0,message)
    request.session['gold'] = gold_to_add + request.session['gold']
    return redirect("/")