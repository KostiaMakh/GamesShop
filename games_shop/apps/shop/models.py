from django.db import models
from django.urls import reverse
from slugify import slugify


class BaseModel(models.Model):
    slug = models.CharField(max_length=256)
    title = models.CharField(max_length=240)

    def __str__(self):
        return self.title

    def save(self):
        super(BaseModel, self).save()
        self.slug = f'{self.pk}-{slugify(str(self.title))}'
        super(BaseModel, self).save()

    class Meta:
        ordering = ('title',)
        abstract = True


class Genre(BaseModel):
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',
                              blank=True)

    def get_absolute_url(self):
        return reverse('genre', kwargs={'slug': self.slug})


class Game(BaseModel):
    description = models.TextField()
    poster = models.ImageField(upload_to='photos/%Y/%m/%d',
                               blank=True)
    release_year = models.DateField()
    companies = models.ForeignKey('Company',
                                  on_delete=models.PROTECT)
    languages = models.ManyToManyField('Language')
    devices = models.ManyToManyField('Device')
    genres = models.ForeignKey('Genre',
                               on_delete=models.PROTECT)
    promos = models.ManyToManyField('Promo',
                                    blank=True)
    price = models.PositiveIntegerField()
    old_price = models.PositiveIntegerField(default=0,
                                            blank=True)
    buys = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey('user.User',
                              on_delete=models.CASCADE,
                              default=1)
    is_published = models.BooleanField(default=False)
    status = models.ForeignKey('Status',
                               on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('game', kwargs={'slug': self.slug})


class ScreenShot(models.Model):
    game = models.ForeignKey('Game',
                             on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='photos/%Y/%m/%d',
                                   blank=True)


class Status(models.Model):
    status = models.CharField(max_length=128)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'Statuses'


class Company(BaseModel):
    description = models.TextField()
    foundation = models.DateField()
    logo = models.ImageField(upload_to='photos/%Y/%m/%d',
                             blank=True)

    def get_absolute_url(self):
        return reverse('company', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Companies'


class Language(BaseModel):
    pass


class Device(BaseModel):
    pass


class Promo(BaseModel):
    description = models.TextField()
    banner = models.ImageField(upload_to='photos/%Y/%m/%d',
                               blank=True)
    start_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)
