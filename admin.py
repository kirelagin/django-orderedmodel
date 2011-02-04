# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls.defaults import patterns
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class OrderedModelAdmin(admin.ModelAdmin):
  ordering = ['order']
  exclude = ['order']

  def get_urls(self):
    my_urls = patterns('',
        (r'^(?P<pk>\d+)/move_up/$', self.admin_site.admin_view(self.move_up)),
        (r'^(?P<pk>\d+)/move_down/$', self.admin_site.admin_view(self.move_down)),
    )
    return my_urls + super(OrderedModelAdmin, self).get_urls()

  def reorder(self, item):
    button = '<a href="%s">-%s-</a>'

    html = ''
    html += button % ('%d/move_down/' % item.pk, '↓')
    html += button % ('%d/move_up/' % item.pk, '↑')
    return html
  reorder.allow_tags = True

  def move_down(self, request, pk):
    if self.has_change_permission(request):
      item = get_object_or_404(self.modelClass, pk=pk)
      try:
        next_item = self.modelClass.objects.filter(order__gt=item.order).order_by('order')[0]
      except IndexError: # Last item
        pass
      else:
        self.modelClass.swap(item, next_item)
    return HttpResponseRedirect('../../')

  def move_up(self, request, pk):
    if self.has_change_permission(request):
      item = get_object_or_404(self.modelClass, pk=pk)
      try:
        prev_item = self.modelClass.objects.filter(order__lt=item.order).order_by('-order')[0]
      except IndexError: # First item
        pass
      else:
        self.modelClass.swap(item, prev_item)
    return HttpResponseRedirect('../../')

