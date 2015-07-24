from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

from account.models import Account
from account.forms import AccountForm

# Create your views here.
class Home(TemplateView):
    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
		#import pdb
		#pdb.set_trace() #Python Debuger : hodi identifika ninia sintax error.
        context = super(Home, self).get_context_data()
       	if self.request.user.is_authenticated():  #ita fo seguransa tuir ita hakarak ba pagina Home
             context['accounts'] = Account.objects.filter(user=self.request.user)#katak user sira labele assesu ba malu
        else:
		    context['account'] = None
        return context
#'filter(user=self.request.user)':katak asesu ba ita nia user deit se usa 'all':asesu ba user hotu-hotu nebe ita amenta

class About(TemplateView):
    template_name = 'account/about.html'
    def get_context_data(self, **kwargs):
       	context = super(About, self).get_context_data()
        if self.request.user.is_authenticated():  #ita fo seguransa tuir ita hakarak ba pagina about
            context['accounts'] = Account.objects.filter(user=self.request.user)#katak user sira labele assesu ba malu
        else:
		    context['account'] = None
        return context

class CreateAccount(TemplateView):
	template_name = 'account/create_account.html'

	def get(self, request, *args, **kwargs):
		context = {'account_form' : AccountForm()}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		account_form = AccountForm(request.POST)

		if account_form.is_valid():
			#user = account_form.cleaned_data['user']
			#user = self.request.user
			name = account_form.cleaned_data['name']
			amount = account_form.cleaned_data['amount']
			active = account_form.cleaned_data['active']
			#account = Account(user=user, name=name, amount=amount, active=active)
			account = Account(user=self.request.user, name=name, amount=amount, active=active)
			account.save()
			
			return HttpResponseRedirect('/')
		else:
			context = {'account_form': account_form}
			return render(request, self.template_name, context)

