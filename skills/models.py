from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('skills/images/')
    pdf_file = models.FileField(upload_to='skills/pdf/', blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

