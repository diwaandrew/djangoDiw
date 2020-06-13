from rest_framework import generics, mixins, permissions
from ..models import References
from .serializers import ReferencesSerializer
from .permissions import IsAuthorOrReadonly
from django.utils.text import slugify

class ReferencesListView(generics.ListCreateAPIView):
    queryset = References.objects.all()
    # print(queryset)
    serializer_class = ReferencesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user, slug=slugify(serializer.validated_data['title'], allow_unicode=True))

class ReferencesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = References.objects.all()
    # print(queryset)
    serializer_class = ReferencesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadonly]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save(slug=slugify(serializer.validated_data['title'], allow_unicode=True))