import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Workstation(models.Model):
    muid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    w_name = models.CharField("workstation name", max_length=9, blank=True)
    slug = models.SlugField(max_length=9, unique=True, blank=True)
    belarc_file = models.FileField(upload_to="belarc_files/", blank=True)
    anti_virus = models.CharField("anti-virus", max_length=100, blank=True)
    os_build = models.CharField("operating system", max_length=100, blank=True)
    installed = models.TextField("apps installed", blank=True)
    network_speed = models.CharField("network speed", max_length=100, blank=True)
    is_installed = models.BooleanField("is adobe reader installed", default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.w_name)
        super(Workstation, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("machines:detail", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self):
        return self.w_name

class Belarc(models.Model):
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to="install_belarc/", blank=True)
    
    def __str__(self):
        return self.file_name