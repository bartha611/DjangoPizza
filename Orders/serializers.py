from Menu.models import MenuItem
from .models import CartItem
from rest_framework import serializers
from Menu.serializers import MenuItemSerializer
from Profile.serializers import ProfileSerializer


class CartItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    user = ProfileSerializer(read_only=True)

    def create(self, validated_data):
        menu_item_data = validated_data.pop('menu_item')
        menu_item = MenuItem.objects.get(id=menu_item_data)
        return CartItem.objects.create(menu_item=menu_item)

    class Meta:
        model = CartItem
        fields = ('user', 'menu_item', 'createdat',)
