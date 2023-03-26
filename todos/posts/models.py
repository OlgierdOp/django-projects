from django.db import models
from common.models import Timestamped

# Create your models here.





class Post(Timestamped):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField("tags.Tag", related_name="posts", blank=True)
    img = models.ImageField(upload_to="posts/images/%Y/%m/%d/", blank=True, null=True, width_field="img_width")
    img_width = models.IntegerField(blank=True, null=True, editable=False)
    datafile = models.FileField(upload_to="posts/files/%Y/%m/%d/",  blank=True, null=True)

    @property
    def datafile_name(self):
        name = ""
        if self.datafile:
            name = self.datafile.name.split("/")[-1]
        return name

    def __str__(self): return f"{self.title}"

    # class Meta:
    #     verbose_name_plural = "renifer"
