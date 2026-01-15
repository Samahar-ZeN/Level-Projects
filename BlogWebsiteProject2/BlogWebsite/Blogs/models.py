from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse



# Create your models here.
#............ContactusPage-Model..............#
class contactuspage(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()






#.............BlogsPosts-Model..............#
class blogspost(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('blogsdetailshow', kwargs={'pk': self.pk})




#..............ProfilePage-model...............#
class profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

def __str__(self):
    return f'{self.user.username} profile'





































































































