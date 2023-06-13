from django.core.mail import send_mail
from dotenv import load_dotenv
import os
import random

from fsd_medic.settings import BASE_DIR
import random
from .models import Countries
load_dotenv(BASE_DIR / ".env")


def Send_email(user_email, message):
    send_mail(
        'Подтверждение почты',
        message,
        os.getenv("EM_HOST_USER"),
        [user_email],
        fail_silently=False,
    )

def create_or_delete(classmodel, **kwargs):
    try:
        obj = classmodel.objects.get(**kwargs)
        obj.delete()
    except:
        obj = classmodel.objects.create(**kwargs)
        obj.save()


def generate_email_code():
    code = random.randrange(start=10000000, stop=99999999)
    return code


def get_number_code_list():
    choises_list = []
    for item in Countries.objects.all():
        choises_list.append([item.number_code + '/' + item.number_length, f'{item.name}  {item.number_code}'])
    return choises_list
