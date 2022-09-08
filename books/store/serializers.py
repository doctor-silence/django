from rest_framework.serializers import ModelSerializer

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        filds = '__all__'
