from favorite.models import Category, Thing
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.serializers import ValidationError


class HistoricalRecordsSerializer(ModelSerializer):
    def __init__(self, model,  *args, fields='__all__', **kwargs):
        self.Meta.model = model
        self.Meta.fields = fields
        super().__init__()

    class Meta:
        pass


class CategorySerializer(ModelSerializer):
    history = SerializerMethodField()

    class Meta:
        model = Category
        fields = ('__all__')
        read_only_fields = ('id', 'history')

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = ['history_id', 'id', 'name', 'history_date', 'history_type']
        serializer = HistoricalRecordsSerializer(
            model, obj.history.all().order_by('history_date'), fields=fields,
            many=True)
        serializer.is_valid()
        return serializer.data


class ThingSerializer(ModelSerializer):
    category_name = SerializerMethodField()
    history = SerializerMethodField()

    class Meta:
        model = Thing
        fields = ('id', 'description', 'title', 'ranking', 'category_name',
                  'meta', 'category', 'created_at', 'updated_at', 'history')
        read_only_fields = ('id', 'category_name', 'history')

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = ['history_id', 'history_date', 'history_type']
        serializer = HistoricalRecordsSerializer(
            model, obj.history.all().order_by('history_date'), fields=fields,
            many=True)
        serializer.is_valid()
        return serializer.data

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
            ranking__exact=validated_data['ranking']
        ).order_by('ranking').count()
        print(validated_data.get('category').thing_set.order_by('ranking'))
        # return 'self'
        if things_count == 0:
            obj = super().create(validated_data)
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
