from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from forms import ContactForm
# Create your views here.


def contact(request):
    contactform = ContactForm()
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            message = contactform.save(commit=False)
            message.save()
            return HttpResponseRedirect(reverse("contact"))
        else:
            print(contactform.errors)

    return render(request,"contact_form/contact.html",{"contactform":contactform})
