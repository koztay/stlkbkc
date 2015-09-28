from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model
from braces import views as bracesviews
# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from . models import Comment
from . forms import CommentForm
from profiles.models import BabySitterProfile, ParentProfile

User = get_user_model()

class CommentCreateView(bracesviews.LoginRequiredMixin,
                 bracesviews.FormValidMessageMixin,
                 CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'comments/comment_create.html'
    success_url = reverse_lazy('profiles:parent-profile-list')
    form_valid_message = "You're commented up!"

    def form_valid(self, form):
		#print self.kwargs #buradan object id'yi aliyoruz.
		profile_id = self.kwargs['object_id']
		commented_user = User.objects.get(pk=profile_id)
		#print commented_user
		form.instance.commented_user=commented_user
		form.instance.user = self.request.user

		return super(CommentCreateView, self).form_valid(form)


class CommentListView(bracesviews.LoginRequiredMixin, ListView):
        template_name = "comments/show_comments.html"
        model = Comment
        http_method_names = ['get']

        def get(self, request, *args, **kwargs):
            pk = kwargs['pk']
            user = User.objects.get(pk=pk)
            kwargs['user']=user
            self.object_list = Comment.objects.all_for_commented_user(user)
            context = self.get_context_data(comments=self.object_list)
            return self.render_to_response(context)

            