# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import re


class OrderedModelAdmin(admin.ModelAdmin):
  ordering = ['order']
  exclude = ['order']
  filter_expr = re.compile("(.*)__(.*)__exact")

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
    filter_column = None
    filter_key = None
    filter_val = None

    # check if view is filtered
    for key in request.GET:
      try:
        filter_column, filter_key = OrderedModelAdmin.filter_expr.search( key ).groups()
        filter_val = request.GET.get(key)
        print "k:", filter_column, filter_key
      except:
        continue

    if self.has_change_permission(request):
      item = get_object_or_404(self.model, pk=pk)
      try:
        query_args = {}
        query_args['order__gt']=item.order
        if ( filter_key != None and filter_column != None ):
          query_args[filter_column]=filter_val
        next_item = self.model.objects.filter(**query_args).order_by('order')[0]
      except IndexError: # Last item
        pass
      else:
        self.model.swap(item, next_item)
    return HttpResponseRedirect('../../?' + request.GET.urlencode())

  def move_up(self, request, pk):
    filter_column = None
    filter_key = None
    filter_val = None

    # check if view is filtered
    for key in request.GET:
      try:
        filter_column, filter_key = OrderedModelAdmin.filter_expr.search( key ).groups()
        filter_val = request.GET.get(key)
        print "k:", filter_column, filter_key
      except:
        continue

    if self.has_change_permission(request):
      item = get_object_or_404(self.model, pk=pk)
      try:
        query_args = {}
        query_args['order__lt']=item.order
        if ( filter_key != None and filter_column != None ):
          query_args[filter_column]=filter_val
        prev_item = self.model.objects.filter(**query_args).order_by('-order')[0]
      except IndexError: # First item
        pass
      else:
        self.model.swap(item, prev_item)
    #print dir(request.GET)
    return HttpResponseRedirect('../../?' + request.GET.urlencode())

