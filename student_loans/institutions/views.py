from rest_framework import permissions, viewsets

from .models import Award, Institution
from .serializers import AwardSerializer, InstitutionSerializer


class InstitutionsApiViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows all institutions to be viewed
    """

    queryset = Institution.objects.all().order_by("-created_at")
    serializer_class = InstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]


class AwardApiViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows awards to be viewed
    """

    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    permission_classes = [permissions.IsAuthenticated]
