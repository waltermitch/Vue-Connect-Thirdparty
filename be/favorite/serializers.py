from favorite.models import Category, Thing
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.serializers import ValidationError


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        read_only_fields = ('id',)


class ThingSerializer(ModelSerializer):
    category_name = SerializerMethodField()

    class Meta:
        model = Thing
        fields = ('id', 'description', 'title', 'ranking', 'category_name',
                  'meta', 'category', 'created_at', 'updated_at')
        read_only_fields = ('id', 'categgory_name')

    def validate_decription(self, value):
        if len(value) != 0 and len(value) < 10:
            raise ValidationError(
                "When description is not empty, mininmum length is 10 \
                characters.")
        return value

    def get_category_name(self, obj):
        return obj.category.name

    def create(self, validated_data):
        print(validated_data)
        things_count = validated_data['category'].thing_set.filter(
            ranking__exact=validated_data['ranking']).order_by('ranking').count()
        print(validated_data.get('category').thing_set.order_by('ranking'))
        # return 'self'
        if things_count == 0:
            obj = super().create(valiated_data)
            return obj
        things = validated_data['category'].thing_set.order_by(
            'ranking')
        for thing in things:
            if thing.ranking >= validated_data['ranking']:
                thing.ranking += 1
                thing.save()
        obj = super().create(validated_data)
        things = validated_data['category'].thing_set.order_by('ranking')
        return obj

    def update(self, instance, validated_data):
        things_count = validated_data['category'].thing_set.filter(
            ranking__exact=validated_data['ranking']
        ).order_by('ranking').count()

        if things_count == 0:
            obj = super().update(instance, validated_data)
            return obj
        things = validated_data['category'].thing_set.all().order_by('ranking')
        for thing in things:
            if thing.ranking >= validated_data['ranking']:
                thing.ranking += 1
                thing.save()
        obj = super().update(instance, validated_data)
        return obj
