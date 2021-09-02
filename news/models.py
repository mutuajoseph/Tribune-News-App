from django.db import models

# Create your models here.
# editor model
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name
    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()
    
    def delete_editor(self, first_name):
        self.objects.filter(self.first_name == first_name).delete()

# tags model
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

# article model
class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)