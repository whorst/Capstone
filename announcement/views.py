from django.shortcuts import render
from models import Announcement


def home(request):
    announcements = Announcement.objects.order_by("-id")[:5]
    #The above code will return the last five items in the QuerySet as ordered by Primary Key

    return render(request, "test_app/home.html",{"announcements":announcements})
