  
from django.shortcuts import reverse, redirect, render
from django_google.flow import DjangoFlow,CLIENT_SECRET_FILE, SCOPES
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.conf import settings
from django_google.models import GoogleAuth
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


def forms(request):
    return render(request, 'sbuddy/forms.html')