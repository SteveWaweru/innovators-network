from django.db import IntegrityError
from django.shortcuts import render
from django.views.generic import View
from .models import Mail


class Home(View):
    template_name = 'dashboard/index.html'
    message = 'Your Email has been saved successfully. Thank you for your subscription.'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        try:
            user_email = Mail.objects.create(email=request.POST.get('email'))
            user_email.save()
        except IntegrityError as e:
            self.message = 'We envy your excitement. Thank you, but we already have your mail with us.'
        return render(request, self.template_name, {'success': self.message })
