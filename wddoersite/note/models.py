from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=128)
    pub_time = models.DateTimeField(auto_now_add=True)
    po_type = models.ForeignKey(Category, verbose_name='category', blank=True, null=True)
    content = models.TextField()

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.title