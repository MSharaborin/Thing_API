import base64
from django.shortcuts import render, HttpResponse
from.models import PicturePerson
from PIL.Image import Image
from io import BytesIO


def index(request):
    # image = PicturePerson.objects.all()
    # count = 0
    # for i in image:
    #     count += 1
    #     data = base64.b64decode(i.binary_picture)
    #     with open('image/img' + str(count) + '.jpg', 'wb') as f:
    #         f.write(data)
    #
    # context = {
    #     'image': image
    # }
    return HttpResponse('<h1>Telegram BOT API v_0.1</h1>')
