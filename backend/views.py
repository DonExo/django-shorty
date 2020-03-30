from django.shortcuts import render, redirect, get_object_or_404

from .models import Shortener
from .forms import FormShortener


def index(request):
    if request.method == 'POST':
        form = FormShortener(request.POST)
        host = request.get_raw_uri()
        if form.is_valid():
            # We don't actually care about the form at this moment, but just the URL value
            form_obj = form.save(commit=False)

            shortener, created = Shortener.objects.get_or_create(original_url=form_obj.original_url)
            # Place for assigning User logic to the shorteners
            return render(request,
                          "backend/index.html",
                          {'form': form,
                          'result': shortener.short_url,
                          'host': host,
                          'created': created})

    form = FormShortener()
    return render(request, "backend/index.html", {'form': form})

def redirecto(request, shorty):
    object = get_object_or_404(Shortener, short_url=shorty)
    object.times_visited += 1
    object.save()
    return redirect(object.original_url)