from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class RawHtmlPlugin(CMSPlugin):

    body = models.TextField('HTML')

    def __str__(self):
        return self.body
