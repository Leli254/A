from django.db import models
from django.conf import settings
from django.utils.text import slugify


class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True,on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/category/%s/" % self.slug
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PostCategory, self).save()




class PostTag(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,default='')
    description=models.TextField()
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        
        
    def __str__(self):
        return self.name
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PostTag, self).save()

    


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name=('blog_posts'))
    content = models.TextField()
    category = models.ManyToManyField(PostCategory,related_name='category')
    tag=models.ManyToManyField(PostTag,related_name='tag')
    status = models.IntegerField(choices=STATUS, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post Article'
        verbose_name_plural = 'Post Articles'
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save()
