from django.shortcuts import render
from .models import Post
from django.core.mail import send_mail
# json
from django.views.generic import TemplateView, View
from django.core import serializers
from django.http import JsonResponse


# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'index.html', context)


def success(request):
    context = {}
    return render(request, 'success.html', context)


def main(request):
    context = {}
    return render(request, 'main.html', context)


class PostView(View):
    def get(self, request):
        qs = Post.objects.all()
        data = serializers.serialize('json', qs)
        return JsonResponse({'data': data}, safe=False)


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # SEND
        send_mail(
            message_name,
            message,
            message_email,
            ['tadedonline@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'success.html', {'message_name': message_name})

    else:
        return render(request, 'home.html', {})