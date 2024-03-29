from django.db import models
from django.urls import reverse
from django.utils.timezone import now

def set_duration(date):
    duration = str(date-now().date())
    return duration


class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    slug = models.SlugField(max_length=150, unique=True)
    poster = models.ImageField(upload_to='uploads/film/film-poster', default='uploads/None/no-img.jpg')
    trailer_youtube_link = models.CharField(null=True, blank=True, max_length=400)
    show_today = models.BooleanField(default=False)
    show_soon = models.BooleanField(default=False)
    show_soon_from_date = models.DateField(null=True, blank=True)
    show_soon_to_date = models.DateField(null=True, blank=True)
    show_now_to_date = models.DateField(null=True, blank=True)
    can_sell_ticket = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('theater:film_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = "Фільми"

class FilmShowSession(models.Model):
    session = models.DateTimeField(null=True, blank=True)
    three_d = models.BooleanField(default=True, verbose_name='3D сеанс')
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return u'%s' % self.since.strftime('%Y-%m-%d %H:%M')


class FilmImages(models.Model):
    image = models.ImageField(upload_to='uploads/film/film-gallery', default='uploads/None/no-img.jpg')
    film = models.ForeignKey('Film', blank=True, null=True, on_delete=models.CASCADE)

class FilmDescription(models.Model):
    year = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    screenwriter = models.CharField(max_length=150)
    producer = models.CharField(max_length=150)
    operator = models.CharField(max_length=150)
    composer = models.CharField(max_length=150)
    budget = models.IntegerField()
    duration = models.CharField(max_length=150)
    age = models.CharField(max_length=10)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)



class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='uploads/news/', default = 'uploads/None/no-img.jpg')
    slug = models.SlugField(unique=True, max_length=250, null=True)
    date = models.DateTimeField(verbose_name='Дата додавання новини', auto_now=True, blank=True, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новини"

    def get_short_body(self):
        return self.body[0:100]
    
    def get_absolute_url(self):
        return reverse('theater:news_detail', kwargs={'slug': self.slug})