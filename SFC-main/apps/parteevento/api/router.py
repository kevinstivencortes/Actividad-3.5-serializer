from rest_framework.routers import DefaultRouter

from apps.parteevento.api.views import ParteEventoViewSet

from apps.parteevento.api.views import ParteEvento_registrar

router_parteEvento = DefaultRouter()
router_parteEvento.register(prefix="parteEvento", basename="parteEvento", viewset=ParteEventoViewSet)
router_parteEvento.register(prefix="parteEventoRegistrar", basename="parteEventoRegistrar", viewset=ParteEvento_registrar)