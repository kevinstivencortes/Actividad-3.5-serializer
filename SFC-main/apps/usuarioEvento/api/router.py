from rest_framework.routers import DefaultRouter
from apps.usuarioEvento.api.views import EventoViewSet

from apps.usuarioEvento.api.views import EventoRegistrar

router_usuarioEvento = DefaultRouter()
router_usuarioEvento.register(prefix='usuarioEvento', basename='usuarioEvento', viewset=EventoViewSet)
router_usuarioEvento.register(prefix='usuarioEventoRegistrar', basename='usuarioEventoRegistrar', viewset=EventoRegistrar)