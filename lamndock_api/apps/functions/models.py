from __future__ import unicode_literals

from django.db import models


class Stack(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    docker_image = models.CharField(max_length=1000)

    def __unicode__(self):
        return '{} - {}'.format(self.name, self.description)


class Function(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    stack = models.ForeignKey('functions.Stack')
    timeout = models.FloatField(help_text='Maximum function execution time in milliseconds')

    def __unicode__(self):
        return '{} - {}'.format(self.name, self.description)


class FunctionVersion(models.Model):
    class Meta:
        unique_together = (('id', 'version'),)

    function = models.ForeignKey('functions.Function')
    body = models.TextField()
    version = models.CharField(max_length=10)

    def __unicode__(self):
        return '{} - v{}'.format(self.function, self.version)
