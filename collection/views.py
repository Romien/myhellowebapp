from django.shortcuts import render, redirect

from collection.forms import ThingForm
from collection.models import Thing

# Create your views here.


def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', {
        "things": things,
    })
# our new view:


def thing_detail(request, king):
    # grab the object...
    thing = Thing.objects.get(slug=king)

    # and pass to the temlplate
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })


def edit_thing(request, king):
    # grab the object...
    thing = Thing.objects.get(slug=king)
    # set the form we're using
    form_class = ThingForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', king=thing.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    # and render the template
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })
