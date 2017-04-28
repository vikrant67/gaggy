from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm, UploadForm
from .models import Upload, Liked, Comment
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template import defaultfilters


IMAGE_FILE_TYPES = ['mp4','png', 'jpg', 'jpeg','gif']
VIDEO_TYPE=['mp4','3gp']
MAX_UPLOAD_SIZE = "2621440 "


def index(request):
    user = request.user
    data = Upload.objects.all()

    liked=list(Liked.objects.filter(user=user.id).values_list('like_id',flat=True))

    return render(request, 'gag/index.html', {'user':user,'data':data,'liked':liked})


def detail(request, pk):
    user = request.user
    content = Upload.objects.get(pk=pk)
    
    liked=list(Liked.objects.filter(user=user.id).values_list('like_id',flat=True))
    all_comments = Comment.objects.filter(upload_id=pk).order_by('comment_time')

    return render(request, 'gag/details.html', {'user': user, 'content': content, 'liked': liked, 'all_comments': all_comments})


class UserFormView(View):
    form_class = UserForm
    template_name='gag/register.html'

    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    #process the data and store it into the dataindex
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            #cleaned data<normalized>

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)

            user.save()


        user=authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/gag/',{'user':user})

        return render(request,self.template_name,{'form':form})



def login_user(request):
    username=request.GET['username']
    password=request.GET['password']

    user=authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request,user)
            data = {
            'is_login': True
            }
    else:
        data = {
        'is_login': False
        }
    return JsonResponse(data)

    




def logout_user(request):
    logout(request)
    user=request.user
    data=Upload.objects.all()
    return redirect('/gag/',{'user':user,'data':data})


#owner register form

class UploadFormView(View):
    form_class= UploadForm
    template_name='gag/upload.html'

    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
     #process the data and store it into the dataindex
    def post(self,request):
        form=self.form_class(request.POST,request.FILES)



        if form.is_valid():

            user=form.save(commit=False)
            
            #cleaned data<normalized>

            
            
            
            file_type = user.media.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                form=self.form_class(None)
                context = {
                    'form':form,
                    
                    'error': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request,self.template_name,context)
            file=form.cleaned_data['media']

            if int(file.size) > int(MAX_UPLOAD_SIZE):
                form=self.form_class(None)
                context = {
                    'form':form,
                    'error': 'file size should be less than 2.5mb',
                }
                return render(request,self.template_name,context)
            user.user=request.user
            user.file_format=file_type
            firstname=User.objects.get(username=request.user)
            user.firstname=firstname.first_name
            count=0
            for account in request.user.socialaccount_set.all():
                if(request.user== account.user):
                    count=1
                    user.user_pic=account.extra_data.get('picture')

            if count==0:
                user.user_pic="/static/gag/images/user.jpg"


            user.save()
            
            user=request.user
            
            data=Upload.objects.all()
            
            context = {

                    'user':user,
                    'data':data,
                    
                    'video_type':VIDEO_TYPE,
                    

                }
            return redirect('/gag/',context)


       

        return render(request,self.template_name,{'form':form})


def like(request):
    
    selected_post=Upload.objects.get(pk=request.GET['post'])

    s=selected_post.like+1
    selected_post.like=s
    selected_post.save()

    new=Liked(like_id=request.GET['post'],description=selected_post.description)
    new.user=request.user
    new.save()


    data = {
        'is_done': selected_post.like
    }
    return JsonResponse(data)


def dislike(request):
    
  
    
    selected_post=Upload.objects.get(pk=request.GET['post'])

    s=selected_post.like-1
    selected_post.like=s
    selected_post.save()
    user=request.user
    new=Liked.objects.get(like_id=request.GET['post'],user=user.id)
    
    new.delete()

    data = {
        'is_done': selected_post.like
    }
    return JsonResponse(data)


def post_comment(request):
    post_id = request.GET['post_id']
    cmnt = request.GET['cmnt']
    user = request.user
    k = False
    time=""
    if not cmnt.isspace():
        c = Comment(upload_id=post_id, user=user, comment=cmnt)

        c.save()
        cmnts = Comment.objects.get(pk=c.id)
        time=defaultfilters.timesince(cmnts.comment_time)
        

        k = True

    data = {
        'is_done': k,
        'time':time
    }
    return JsonResponse(data)


def show_comments(request):
    post_id = request.GET['post_id']
    cmnts = Comment.objects.filter(upload_id=post_id).order_by('-comment_time')
    query_count = cmnts.count()
    all_cmnts = cmnts[:2][::-1]
    results = []
    for cmnt in all_cmnts:
        cmnt_json = {}
        cmnt_json['username'] = cmnt.user.username
        cmnt_json['comment'] = cmnt.comment
        cmnt_json['comment_time'] = defaultfilters.timesince(cmnt.comment_time)


        results.append(cmnt_json)
    data = {
        'all_cmnts': results,
        'total_cmnts': query_count
    }
    return JsonResponse(data)                               