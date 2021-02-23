from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RideForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def ride_list(request):
    if request.method == 'POST':
        form = RideForm(data=request.POST)
        if form.is_valid():
            # log in user next time
            form.save()
    else:
        form = RideForm()
    return render(request, 'offerride/ride.html', {'form': form})
