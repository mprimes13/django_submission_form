from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Personal

# Create your views here.
def index(request):
    err = request.GET.get("error", None)
    return render(request, 'submission_form/index.html', {'error': err})

def submit(request):
    if request.POST:
        req = request.POST
        if len(req['name'].strip(' ')) == 0 or len(req['title'].strip(' ')) == 0:
            return HttpResponseRedirect('/?error=Name or Title Must be populated by characters other than whitespaces.')

        p = Personal(name=req['name'].strip(), title=req['title'].strip(), age=req['age'], hometown=req['hometown'].strip())
        p.save()
    return HttpResponseRedirect(f'confirmation/{p.id}')

def confirmation(request, entry_id=None):
    params = {'results_list': Personal.objects.order_by('-id')}
    if request.GET.get('id', None) or entry_id:
        params['cfrm_obj'] = Personal.objects.get(pk=request.GET.get('id', entry_id))
    return render(request, 'submission_form/confirmation.html', params)
