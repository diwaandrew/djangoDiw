from rest_framework import serializers
from ..models import References

class ReferencesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = References
        fields = ['id', 'title', 'slug', 'description', 'link', 'author']