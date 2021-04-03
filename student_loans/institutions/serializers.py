from rest_framework import serializers

from .models import Award, Institution


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ["id", "name", "state", "zip", "type", "source_id"]


class AwardSerializer(serializers.ModelSerializer):
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


class AwardSummarySerializer(serializers.Serializer):
    loans_originated_count = serializers.IntegerField()
    loans_originated_amount = serializers.FloatField()
    receipient_count = serializers.IntegerField()
    disbursements_amount = serializers.FloatField()
    disbursements_count = serializers.IntegerField()


class QuarterAwardSerializer(AwardSummarySerializer):
    quarter = serializers.IntegerField()
    year = serializers.IntegerField()


class SummarySerializer(serializers.Serializer):
    total = AwardSummarySerializer()
    quarterly = QuarterAwardSerializer(many=True)
