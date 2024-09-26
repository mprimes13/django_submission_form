from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Personal
from .forms import SubmissionForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            p = Personal(**form.cleaned_data)
            p.save()
            return HttpResponseRedirect(f'confirmation/{p.id}')
        else:
            return HttpResponseRedirect('/?error=Name or Title Must be populated by characters other than whitespaces.')
    else:
        err  = request.GET.get("error", None)
        form = SubmissionForm()
        return render(request, 'submission_form/index.html', {'error': err, 'form': form})

def confirmation(request, entry_id=None):
    params = {'results_list': Personal.objects.order_by('-id')}
    if request.GET.get('id', None) or entry_id:
        params['cfrm_obj'] = Personal.objects.get(pk=request.GET.get('id', entry_id))
    return render(request, 'submission_form/confirmation.html', params)
