from django.shortcuts import render
from django.views.generic import View
from .models import Mail


class Home(View):
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        user_email = Mail.objects.create()
        user_email.email = request.POST.get('email')
        user_email.save()
        return render(request, self.template_name, {'success': 'Your Email has been saved successfully. Thank you for '
                                                               'your subscription. '})
