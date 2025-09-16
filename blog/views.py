from django.shortcuts import render
import datetime
from django.utils import timezone
from user_agents import parse


def index(request):
    return render(request, 'blog/index.html')

def uzbekistan(request):
    return render(request, 'blog/uzb.html')

def current_time(request):
    now = datetime.datetime.now()
    return render(request, 'blog/curr_time.html', {"now": now})

def device(request):
    ua_string = request.META.get('HTTP_USER_AGENT', 'Unknown')
    user_agent = parse(ua_string)

    ip_address = request.META.get('REMOTE_ADDR')
    visit_time = timezone.now()

    context = {
        "device_type": "Mobile" if user_agent.is_mobile else "Tablet" if user_agent.is_tablet else "PC",
        "os": user_agent.os.family + " " + user_agent.os.version_string,
        "browser": user_agent.browser.family + " " + user_agent.browser.version_string,
        "ip_address": ip_address,
        "visit_time": visit_time,
    }
    return render(request, 'blog/device.html', {"device": user_agent})
