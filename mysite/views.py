from django.shortcuts import reverse, redirect, render
from django_google.flow import DjangoFlow,CLIENT_SECRET_FILE, SCOPES
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.conf import settings
from django_google.models import GoogleAuth

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

User = get_user_model()

flow = DjangoFlow.from_client_secrets_file(client_secrets_file=CLIENT_SECRET_FILE, scopes=SCOPES)

# Auto Redirect to Google Authentication URL (Using Without Javascript)
def oAuthView(request):
        callback_url=reverse("oauth2callback") # callback Url (oAuth2CallBackView URL)
        return redirect(flow.get_auth_url(request, callback_url=callback_url))

# Google Authentication Call Back VIEW (Using Without Javascript)
def oAuth2CallBackView(request):
    success_url = "/dashboard/"  # redirection URL on Success reverse() can b use here
    creds = flow.get_credentails_from_response_url(response_url=request.build_absolute_uri())
    userinfo = flow.get_userinfo(creds=creds)
    try:
        user = User.objects.get(email=userinfo['email'])
    except User.DoesNotExist:
        user = User.objects.create(email=userinfo['email'],
                                           username=userinfo['email'],
                                           first_name=userinfo['given_name'],
                                           last_name=userinfo['family_name']
                                       )
    finally:
        try:
            gauth = GoogleAuth.objects.get(user=user)
        except GoogleAuth.DoesNotExist:
            gauth = GoogleAuth.objects.create(user=user, creds=creds)

    # Return Response as you want or Redirect to some URL

def oAuthJavascriptView(request):
    if request.is_ajax():
        if request.method == "POST":
            code = request.POST.get('code')
            flow = DjangoFlow.from_client_secrets_file(client_secrets_file=CLIENT_SECRET_FILE, scopes=SCOPES)
            creds = flow.get_credentials_from_code(code=code, javascript_callback_url="https://example.org")
            userinfo = flow.get_userinfo(creds=creds)
            try:
                user = User.objects.get(email=userinfo['email'])
            except User.DoesNotExist:
                user = User.objects.create(email=userinfo['email'],
                                               username=userinfo['email'],
                                               first_name=userinfo['given_name'],
                                               last_name=userinfo['family_name']
                                           )
            finally:
                try:
                    gauth = GoogleAuth.objects.get(user=user)
                except GoogleAuth.DoesNotExist:
                    gauth = GoogleAuth.objects.create(user=user, creds=creds)
            # return JSON Response with Status Code of 200 for success and 400 for errors
            return JsonResponse({}, status=200)

    else:
        context = {
            "client_id": getattr(settings, 'GOOGLE_CLIENT_ID', None),
            "scopes": " ".join(SCOPES)
        }
        # Render HTML page that havs Google Authentication Page with Javasccript
        return render(request, 'login.html', context)


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()