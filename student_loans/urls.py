from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from rest_framework_extensions.routers import ExtendedSimpleRouter

from .institutions import views

router = ExtendedSimpleRouter()
(
    router.register(
        r"institutions", views.InstitutionsViewSet, basename="institutions"
    ).register(
        r"awards",
        views.AwardsViewSet,
        basename="institutions-awards",
        parents_query_lookups=["institution_id"],
    )
)

urlpatterns = [
    path("", include(router.urls)),
    path("summary/", views.SummaryView.as_view()),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
