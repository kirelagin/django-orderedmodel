from django.db import models


class OrderedModel(models.Model):
  order = models.PositiveIntegerField(blank=True, unique=True)

  class Meta:
    abstract = True
    ordering = ['order']

  def save(self):
    if not self.id:
      try:
        self.order = self.__class__.objects.order_by('-order')[0].order + 1
      except:
        self.order = 0
    super(OrderedModel, self).save()
