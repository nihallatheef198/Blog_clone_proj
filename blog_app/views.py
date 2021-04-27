from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from blog_app.models import post,comment
from blog_app.forms import post_form,comment_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DeleteView,
                                    DetailView,CreateView,UpdateView)
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
#default template_name
class about_view(TemplateView):
    template_name = 'about.html'

class post_lst_view(ListView):
    model = post

    def get_queryset(self):
        return post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class post_dtl_view(DetailView):
    model = post

class post_crt_view(CreateView,LoginRequiredMixin):
    model = post
    login_url = '/login/'
    redirect_field_name = '/'
    form_class = post_form

class post_updt_view(UpdateView,LoginRequiredMixin):
    model = post
    login_url = '/login/'
    redirect_field_name = '/'
    form_class = post_form


class post_dlt_view(DeleteView,LoginRequiredMixin):
    model = post
    success_url = reverse_lazy('blog_app:home')


class draft_lst_view(ListView,LoginRequiredMixin):
    model = post
    login_url = '/login/'
    redirect_field_name = '/'

    def get_queryset(self):
        return post.objects.filter(published_date__isnull=True).order_by('create_date')


def add_comment(request,pk):
    if request.method == 'POST':
        posts = get_object_or_404(post,pk=pk)
        form = comment_form(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.post = posts
            comments.save()
            return redirect('blog_app:post_dtl',pk=posts.pk)

    else:
        form = comment_form()

    return render(request,'blog_app/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comments = get_object_or_404(comment,pk=pk)
    comments.approve()
    return redirect('blog_app:post_dtl',pk=comments.post.pk)

@login_required
def comment_dlt(request,pk):
    comments = get_object_or_404(comment,pk=pk)
    post_pk=comments.post.pk
    comments.delete()
    return redirect('blog_app:post_dtl',pk=post_pk)


@login_required
def post_publish(request,pk):
    posts = get_object_or_404(post,pk=pk)
    posts.publish()
    return redirect('blog_app:post_dtl',pk=pk)
