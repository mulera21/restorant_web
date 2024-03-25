from django.shortcuts import render
from django.views import generic
from .models import Item


class MenuList(generic.ListView):
    queryset = Item.object.order_by("-date_created")
    template_name = "index.html"



class MenuItemDetail(generic.ListView):
    model = Item
    template_name = "menu_item_detail.html"

