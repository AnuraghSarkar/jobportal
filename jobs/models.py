from django.db import models
from jobportal import settings
from django.template.defaultfilters import slugify

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    CHOICES = (
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('temporary', 'Temporary'),
    )

    job_type = models.CharField(max_length=20,blank=False,default=None, choices=CHOICES)
    location = models.CharField(max_length=300,blank=False,default=None)
    description = models.TextField(blank=False,default=None)
    publishing_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None,editable=False)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-id',)

