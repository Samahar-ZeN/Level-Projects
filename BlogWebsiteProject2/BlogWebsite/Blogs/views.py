from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Blogs.models import *
from Blogs.forms import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
#.............HomePage-View...............#
def homepage_view(request):
    return render(request, 'home.html')






#..............Home2Page-View................#
@login_required(login_url= 'login')
def home2page_view(request):
    return render(request, 'home2.html')






#..............AboutPage-View.................#
@login_required(login_url='login')
def aboutpage_view(request):
    form1 = contactusform()
    if request.method == 'POST':
        form1 = contactusform(request.POST)
        if form1.is_valid():
            form1.save()
            user1 = form1.cleaned_data.get('name')
            messages.success(request, 'Your message has been submitted!' +   user1)
            return redirect('about')
    context = {'form1' : form1}

    return render(request, 'about.html', context)








#..............SignupPage-View.................#
def signuppage_view(request):
    if request.user.is_authenticated:
        return redirect('home2')
    else:
        form = signuppageform()
        if request.method == 'POST':
            form = signuppageform(request.POST)
            if form.is_valid():
                form.save()
                user1 = form.cleaned_data.get('username')
                messages.success(request, 'You have signedup successfully!' + user1)
                return redirect('login')
    context = {'form' : form}
    return render(request, 'signup.html', context)









#..............LoginPage-View.................#
def loginpage_view(request):
    if request.user.is_authenticated:
        return redirect('home2')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user2 = authenticate(request, username=username, password=password)
            if user2 is not None:
                login(request, user2)
                return redirect('home2')
            else:
                messages.info(request, 'Username or Password is incorrect!')
    context = {}
    return render(request, 'login.html', context)








#.................LogoutPage-View...................#
def logoutpage_view(request):
    logout(request)
    return redirect('login')







#.................ProfilePage-View...................#
@login_required(login_url='login')
def profilepage_view(request):
    return render(request, 'profile.html')







#................UpdateProfilePage-View......................#
@login_required(login_url='login')
def updateprofilepage_view(request):
    if request.method == 'POST':
        fone = updateprofilepageformone(request.POST, instance=request.user)
        ftwo = updateprofilepageformtwo(request.POST, request.FILES, instance=request.user.profile)
        if fone and ftwo.is_valid():
            fone.save()
            ftwo.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile')
    else:
        fone = updateprofilepageformone(instance=request.user)
        ftwo = updateprofilepageformtwo(instance=request.user.profile)
    context = {'fone':fone,'ftwo':ftwo}
    return render(request, 'update_profile.html',context)







#.................BlogsPostsShowPageList-View......................#
class blogspostsshowpagelist_view(LoginRequiredMixin, ListView):
    model = blogspost
    template_name = 'blogspostsshowpage.html'
    context_object_name = 'blog'
    ordering = ['-date_posted']







#................BlogsDetailShowPageList-View....................#
class blogsdetailshowpagelist_view(LoginRequiredMixin, DetailView):
    model = blogspost
    template_name = 'blogs_detail_page.html'








#.................CreateBlogsPage-View......................#
class createblogspage_view(LoginRequiredMixin, CreateView):
    model = blogspost
    fields = ['author', 'title', 'content']
    template_name = 'create_blogs_page.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)








#.................UpdateBlogsPage-View....................#
class updateblogspage_view(UpdateView, LoginRequiredMixin,  UserPassesTestMixin):
    model = blogspost
    fields = ['title', 'content']
    template_name = 'create_blogs_page.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





#....................DeleteBlogsPage-View.........................#
class deleteblogspage_view(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = blogspost
    template_name = 'delete_blogs_page.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    



#....................Finished!!!.......................#






















