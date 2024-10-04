from rest_framework import serializers
from django.utils import timezone
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'price', 'stock']

    # Non-negative price validation
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

    # Non-negative stock validation
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value

    # Future date validation
    def validate_published_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value
