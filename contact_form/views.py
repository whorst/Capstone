from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

from forms import ContactForm

from django.conf import settings

def contact(request):
    contactform = ContactForm()
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            message = contactform.save(commit=False)
            message.save()

            email_subject = "Message From {0} {1}".format(message.first_name, message.last_name)
            email_message = "{0} \n\n {1} \n {2}".format(message.message, message.email, message.phone_number)
            email_sender = settings.EMAIL_HOST_USER

            email = EmailMessage(
                email_subject,
                email_message,
                email_sender,
                [email_sender,],
            )
            email.send()

            return HttpResponseRedirect(reverse("contact"))
        else:
            print(contactform.errors)

    return render(request,"contact_form/contact.html",{"contactform":contactform})
