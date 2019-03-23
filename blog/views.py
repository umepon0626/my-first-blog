from django.shortcuts import render
from blog.form import ContactForm
import sys
from django.core.mail import send_mail, EmailMessage
import smtplib
from blog.mail_submit import create_message


ACCOUNT = "ryuichi.umehara.miraidenshi@gmail.com"
ALIAS = "ryuihi-astrona@ymobile.ne.jp"
PASSWORD = "Ryuichi7"



# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})
    if (request.method == 'POST'):
        subject=request.POST['subject']
        message=request.POST['message']
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [
        "ryuichi-astrona@ymobile.ne.jp"
        ]
        send_mail(subject, message, from_email, recipient_list)
        # msg = create_message(subject,message,sender)

        # s = smtplib.SMTP("smtp.gmail.com", 587)
        # s.ehlo()
        # s.starttls()
        # s.ehlo()
        # s.login(ACCOUNT, PASSWORD)

        # s.sendmail(ACCOUNT, ALIAS, msg.as_string())
        # s.quit()
        # print("postと認識されている")

def contact(request):
    form = ContactForm()
    return render(request, 'blog/contact.html', {
        'form': form.as_table(),
    })


def skill(request):
    return render(request,'blog/skill.html',{})



