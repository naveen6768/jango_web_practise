from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    "january": "Eat no meal for entire month!",
    "february": "Walk for atleast 20 mins everyday!",
    "march": "Dont eat too much junk food",
    "april": "this is a bad month for you",
    "may": "this is great opportunity for me",
    "june": "this is something awesome",
    "july": "this is the rainy season so do it the rice",
    "august": "this is an awesome picture of the wall",
    "september": "this is an epic thoughtful process",
    "october": "this is the elephant",
    "november": "this is a great opportunity to launch a new business",
    "december": "this is an awful conduct by you",

}

def index(request):
    months =list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months":months
    })

def monthly_challenge_by_number(response, month):
    months = list(monthly_challenges.keys())
    if(month > len(months)):
        return HttpResponseNotFound("invalid month")

    forward_months = months[month-1]
    dynamic_path = reverse('monthly-challenge',args = [forward_months])
    return HttpResponseRedirect(dynamic_path)


def monthlyChallenges(request, month):
    try:
        challengeText = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "challenge":month,
            "text":challengeText
        })
    except:
        return Http404()
