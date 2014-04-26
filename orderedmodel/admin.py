# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.admin.views.main import ChangeList


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
    button = '<a href="{{0}}/move_{{1}}/?{{2}}"><img src="{0}orderedmodel/arrow-{{1}}.gif" alt="{{1}}" /></a>'.format(settings.STATIC_URL)

    html = ''
    html += button.format(item.pk, 'down', self.params )
    html += '&nbsp;' + button.format(item.pk, 'up', self.params )
    return html
  reorder.allow_tags = True

  def changelist_view(self, request, extra_context=None):
    self.params = request.GET.urlencode()
    return super(OrderedModelAdmin,self).changelist_view(request, extra_context=extra_context)

  def move_down(self, request, pk):
    cl = self.get_changelist(request)(request, self.model, self.list_display,
                    self.list_display_links, self.list_filter,
                    self.date_hierarchy, self.search_fields,
                    self.list_select_related, self.list_per_page,
                    self.list_max_show_all, self.list_editable, self )

    if self.has_change_permission(request):
      item = get_object_or_404(self.model, pk=pk)
      try:
        next_item = cl.query_set.filter(order__gt=item.order).order_by('order')[0]
      except IndexError: # Last item
        pass
      else:
        self.model.swap(item, next_item)
    return HttpResponseRedirect('../../?' + request.GET.urlencode())

  def move_up(self, request, pk):
    cl = self.get_changelist(request)(request, self.model, self.list_display,
                    self.list_display_links, self.list_filter,
                    self.date_hierarchy, self.search_fields,
                    self.list_select_related, self.list_per_page,
                    self.list_max_show_all, self.list_editable, self )

    if self.has_change_permission(request):
      item = get_object_or_404(self.model, pk=pk)
      try:
        prev_item = cl.query_set.filter(order__lt=item.order).order_by('-order')[0]
      except IndexError: # First item
        pass
      else:
        self.model.swap(item, prev_item)
    return HttpResponseRedirect('../../?' + request.GET.urlencode())

