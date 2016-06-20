from django.shortcuts import render

# Create your views here.

def contact(request):
    #announcements = Announcement.objects.order_by("-id")[:5]
    #The above code will return the last five items in the QuerySet as ordered by Primary Key
    return render(request, "contact_form/contact.html",{})
