from django.db.models import Sum

from rest_framework import permissions, serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Award, Institution
from .serializers import (AwardSerializer, InstitutionSerializer,
                          SummarySerializer)


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


class SummaryView(APIView):
    queryset = Award.objects.all()
    serializer_class = SummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        fq = self.queryset
        if "state" in request.query_params:
            fq = fq.filter(institution__state=request.query_params["state"].upper())
        if "type" in request.query_params:
            if request.query_params["type"] not in Award.LoanType.values:
                raise serializers.ValidationError(
                    {"type": "Please enter a valid loan type."}
                )
            fq = fq.filter(loan_type=request.query_params["type"])

        total = fq.aggregate(
            Sum("receipient_count"),
            Sum("loans_originated_count"),
            Sum("loans_originated_amount"),
            Sum("disbursements_count"),
            Sum("disbursements_amount"),
        )

        quarterly = (
            fq.values("year", "quarter")
            .order_by()
            .annotate(
                Sum("receipient_count"),
                Sum("loans_originated_count"),
                Sum("loans_originated_amount"),
                Sum("disbursements_count"),
                Sum("disbursements_amount"),
            )
        )

        result = {"total": total, "quarterly": quarterly}

        return Response(result)
