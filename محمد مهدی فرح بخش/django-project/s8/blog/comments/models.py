from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.
class Blog(models.Model):
    title = models.CharField(_("عنوان"),max_length=100)
    description = models.CharField(_("توضیحات"),max_length=100)
    content = models.TextField(_("متن"))
    create_at = models.DateTimeField(_("تاریخ انتشار"), default=timezone.now)
    author = models.ForeignKey(User , verbose_name=_("نویسنده"),on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comments(models.Model):
    blog = models.ForeignKey("Blog" , related_name="comments" , verbose_name =_("مقاله"),on_delete=models.CASCADE,blank=True , null=True)
    name = models.CharField(_("نام کاربر"),max_length=100)
    email = models.EmailField(_("آدرس الکترونیکی"),max_length=254)
    message = models.TextField(_("متن نظر"))
    dete = models.DateField(_("تاریخ انتشار") , auto_now=False ,  auto_now_add=True)