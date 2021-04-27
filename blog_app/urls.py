from django.urls import path
from blog_app import views

app_name = 'blog_app'
urlpatterns = [
    path('about/',views.about_view.as_view(),name='about'),
    path('',views.post_lst_view.as_view(),name='home'),
    path('detail/<int:pk>/',views.post_dtl_view.as_view(),name='post_dtl'),
    path('post/create/',views.post_crt_view.as_view(),name='post_new'),
    path('post/update/<int:pk>/',views.post_updt_view.as_view(),name='post_updt'),
    path('post/delete/<int:pk>/',views.post_dlt_view.as_view(),name='post_dlt'),
    path('draft/',views.draft_lst_view.as_view(),name='draft_lst'),
    path('post/comment/<int:pk>/',views.add_comment,name='add_comment'),
    path('post/comment/approve/<int:pk>/',views.comment_approve,name='approve_comment'),
    path('post/comment/rmv/<int:pk>/',views.comment_dlt,name='comment_dlt'),
    path('post/publish/<int:pk>/',views.post_publish,name='post_pub'),

]
