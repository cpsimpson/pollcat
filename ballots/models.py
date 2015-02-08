from django.db import models
from django.conf import settings


class Poll(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    poll = models.ForeignKey('Poll')
    items = models.ManyToManyField('CategoryItem')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class CategoryItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    links = models.ManyToManyField('Link', null=True, blank=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name


class Ballot(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        accepted_string = "not accepted"
        if self.accepted:
            accepted_string = "accepted"
        return "{} - {}".format(self.person, accepted_string)


class Vote(models.Model):
    ballot = models.ForeignKey('Ballot')
    category = models.ForeignKey('Category')
    item = models.ForeignKey('CategoryItem')

    class Meta:
        unique_together = ['ballot', 'category']

    def __str__(self):
        return "{} - {}: {}".format(self.ballot.person, self.category,
                                    self.item)

