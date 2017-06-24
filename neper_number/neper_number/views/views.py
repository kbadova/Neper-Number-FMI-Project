from django.core.management import call_command
from django.views.generic.edit import FormView
from neper_number.forms import CalculateNeperNumberForm
from django.contrib import messages


class CalculateNeperNumberView(FormView):
    form_class = CalculateNeperNumberForm
    template_name = 'calculating.html'
    success_url = '/rsa'

    def form_valid(self, form):
        data = form.cleaned_data

        result = call_command('calculate_neper_number',
                              p=data['members'],
                              t=data['threads'],
                              o=data['output'],
                              q=data['quiet'])

        messages.success(self.request, result)
        return self.form_invalid(form)
