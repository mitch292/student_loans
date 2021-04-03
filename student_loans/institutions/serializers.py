from rest_framework import serializers

from .models import Award, Institution


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = ["id", "name", "state", "zip", "type", "source_id"]


class AwardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        fields = [
            "institution",
            "year",
            "quarter",
            "loan_type",
            "receipient_count",
            "loans_originated_count",
            "loans_originated_amount",
            "disbursements_count",
            "disbursements_amount",
        ]
