from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"
    def get_context_data(self):
        context = {}
        context["meals"] = MEAL_TYPE
        return context
        



class MenuItemDetail(generic.ListView):
    model = Item
    template_name = "menu_item_detail.html"

