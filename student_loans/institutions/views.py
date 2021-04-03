from rest_framework import permissions, viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Award, Institution
from .serializers import AwardSerializer, InstitutionSerializer


class InstitutionsViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows institutions to be viewed
    """

    queryset = Institution.objects.all().order_by("-created_at")
    serializer_class = InstitutionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["state", "zip", "type"]


class AwardsViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows awards to be viewed
    """

    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ["year", "quarter", "loan_type"]
