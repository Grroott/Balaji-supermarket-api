from rest_framework import serializers
from .models import ProductEntry, ProductExit


class ProductEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEntry
        fields = '__all__'


class ProductExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductExit
        fields = '__all__'

    def validate(self, attrs):
        get_instance = self.instance
        product_entry_id_from_request = attrs.get('product_entry').id
        if get_instance is None:  # Logic to validate count if the record to be created
            current_count = ProductEntry.objects.get(id=product_entry_id_from_request).count
            count_validation = True if attrs.get('count') > current_count else False
            if count_validation:
                raise serializers.ValidationError({'buy_product': f'Only {current_count} available in stock!'})

            ProductEntry.objects.filter(id=product_entry_id_from_request).update(
                count=current_count - attrs.get('count'))
        else: # Logic to validate if the record to be updated
            get_original_product_entry_id = self.instance.product_entry.id

            if get_original_product_entry_id != product_entry_id_from_request:  # Logic to validate Foreign key Product
                raise serializers.ValidationError({'buy_product': 'Cannot change the product Name!'})
            get_available_count = ProductEntry.objects.get(id=get_original_product_entry_id).count
            get_current_buy_count = ProductExit.objects.get(id=self.instance.id).count
            count_from_request = attrs.get('count')

            diff = count_from_request - get_current_buy_count
            if diff <= get_available_count:
                ProductEntry.objects.filter(id=product_entry_id_from_request).update(count=get_available_count - diff)
            else:
                raise serializers.ValidationError({'buy_product': f'Only {get_available_count} available in stock!'})

        return attrs
