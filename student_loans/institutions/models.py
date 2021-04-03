import uuid

from django.db import models


class Institution(models.Model):
    class Type(models.TextChoices):
        PUBLIC = "Public"
        PRIVATE_NONPROFIT = "Private Nonprofit"
        PROPRIETARY = "Proprietary"
        FOREIGN_FOR_PROFIT = "Foreign For Profit"
        FOREIGN_PRIVATE = "Foreign Private"
        FOREIGN_PUBLIC = "Foreign Public"
        UNKOWN = "Unknown"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    state = models.CharField(
        max_length=4, blank=True, null=True
    )  # TODO: Can this be an enum or choice
    zip = models.CharField(max_length=12, blank=True, null=True)
    type = models.CharField(max_length=255, choices=Type.choices)
    source_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Award(models.Model):
    class LoanType(models.TextChoices):
        DIRECT_SUBSIDIZED = "direct-loan-subsidized"
        DIRECT_UNSUBSIDIZED_UNDERGRADUATE = "direct-loan-unsubsidized-undergraduate"
        DIRECT_UNSUBSIDIZED_GRADUATE = "direct-loan-unsubsidized-graduate"
        DIRECT_PARENT_PLUS = "direct-loan-parent-plus"
        DIRECT_GRAD_PLUS = "direct-loan-grad-plus"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, blank=True, null=True)
    quarter = models.CharField(max_length=2, blank=True, null=True)
    loan_type = models.CharField(max_length=255, choices=LoanType.choices)
    receipient_count = models.IntegerField(blank=True, null=True)
    loans_originated_count = models.IntegerField()
    loans_originated_amount = models.DecimalField(max_digits=11, decimal_places=2)
    disbursements_count = models.IntegerField(blank=True, null=True)
    disbursements_amount = models.DecimalField(max_digits=11, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.institution}: {self.year}-Q{self.quarter} - {self.loan_type}"
