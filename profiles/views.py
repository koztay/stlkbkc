from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from braces.views import LoginRequiredMixin
from . import forms
from . import models
from . models import ParentProfile, BabySitterProfile
from comments.models import Comment 

User = get_user_model()

class ShowParentProfileList(LoginRequiredMixin, generic.ListView):
    model = ParentProfile
    queryset = ParentProfile.objects.all()
    template_name = "profiles/show_all_profiles.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ShowParentProfileList, self).get_context_data(*args, **kwargs)
        # all_comments = Comment.objects.all()
        # context['comments'] = all_comments
        users_with_comments = []
        for parentprofile in ParentProfile.objects.all():
            #print parentprofile.user
            comments = parentprofile.get_users_comments()
            user_dict = {'profile':parentprofile, 'comments':comments}
            users_with_comments.append(user_dict)
            print comments

        # print kwargs
        context['users_with_comments'] = users_with_comments
        print context
        return context


class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']
    
    """
    It works without the following def get_context_data function. I 
    think it can be useful when it is necessary to edit/modify the 
    context data. 
    Otherwise it is possible to send the model objects as *kwargs and it can be
    available for the teplates. 
    """ 
    # def get_context_data(self, **kwargs):
    #     context = super(ShowProfile, self).get_context_data(**kwargs)
    #     return context

    def get(self, request, *args, **kwargs):

        user = self.request.user
        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user

        try:
            parent_profile = user.parentprofile
            print "%s, %s" %('comments are:', parent_profile.get_users_comments())
            kwargs["parent_profile"] = parent_profile
        except:
            pass

        try:
            babysitter_profile = user.babysitterprofile
            print "%s, %s" %('comments are:',babysitter_profile.get_users_comments())
            kwargs["babysitter_profile"] = babysitter_profile
        except:
            pass


        #print "%s, %s" %('comments are:', parent_profile.get_users_comments())
        #print "%s, %s" %('comments are:',babysitter_profile.get_users_comments(user))
        # print "%s, %s" %("args are : ", args) 
        # print "%s, %s" %("kwargs are : ", kwargs) 
        return super(ShowProfile, self).get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)

        try:
            parent_profile = user.parentprofile
            if "profile_form" not in kwargs:
                kwargs["profile_form"] = forms.ParentProfileForm(instance=parent_profile)
        except:
            pass

        try:
            babysitter_profile = user.babysitterprofile
            if "profile_form" not in kwargs:
                kwargs["profile_form"] = forms.BabySitterProfileForm(instance=babysitter_profile)
        except:
            pass

        # if "profile_form" not in kwargs:
        #     kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)

        try:
            profile = user.parentprofile
            profile_form = forms.ParentProfileForm(request.POST,
                                         request.FILES,
                                         instance=profile)
        except:
            pass

        try:
            profile = user.babysitterprofile
            profile_form = forms.BabySitterProfileForm(request.POST,
                                         request.FILES,
                                         instance=profile)
        except:
            pass

        """
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        """

        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Profile details saved!")
        return redirect("profiles:show_self")
