from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserUpdateForm, UserProfileForm
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for { username }')
			return redirect('blog-home')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})
	
@login_required
def profile(request):
	return render(request, 'users/profile.html')

@login_required
def profileupdate(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			username = user_form.cleaned_data.get('username')
			messages.success(request, f'Account has been Updated for { username }')
			return redirect('profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = UserProfileForm(instance=request.user.profile)

	all_forms = {
		'user_form':user_form, 
		'profile_form':profile_form
		}

	return render(request, 'users/profile_update.html', all_forms )