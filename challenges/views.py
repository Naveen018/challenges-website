from django.shortcuts import redirect, render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Learn Python",
    "february": "Learn Django",
    "march": "Do Django project",
    "april": "Learn Spark",
    "may": "Learn Big data",
    "june": "Do big data project",
    "july": "Learn ML",
    "august": "Learn DL",
    "september": "Do ML projects",
    "october": "Go to andaman",
    "november": "Go to Italy",
    "december": "Celebrate Success",
}


def index(request):

    months_list = list(monthly_challenges.keys())
    return render(request, "index.html", {"all_months": months_list})


def monthly_challenge_by_numbers(request, month):
    months_list = list(monthly_challenges.keys())
    if month > len(months_list):
        return HttpResponseNotFound("Invalid Month!!!")
    redirect_month = months_list[month - 1]
    redirect_url = reverse("string_url", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        challenge_task = monthly_challenges[month]
        return render(
            request, "challenge.html", {"task": challenge_task, "month_name": month}
        )
    except:
        raise Http404()
