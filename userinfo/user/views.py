from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UserInfoForm
from .models import UserInfo


def get_User_info(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.data['first_name'])
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            request.session['user_info'] = form.data
            return redirect('/info/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserInfoForm()

    return render(request, 'user_form.html', {'form': form})


def show_user_info(request):
    data = request.session.get('user_info')

    return render(request, 'user_info.html', {'user': data})
