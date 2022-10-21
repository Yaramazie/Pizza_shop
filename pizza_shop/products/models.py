from django.db import models


class Pizza(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='description')
    price = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Price')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo', blank=True)
    available = models.BooleanField(default=True, verbose_name='Available')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'


class PizzaSlice(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='description')
    price = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Available')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Pizza Slice'
        verbose_name_plural = 'Pizza Slices'


class PizzaRoll(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='description')
    price = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Available')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Pizza Roll'
        verbose_name_plural = 'Pizza Rolls'


class Box(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='description')
    price = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Available')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Box'


class Toping(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='description')
    price = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Available')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Toping'
        verbose_name_plural = 'Topings'
