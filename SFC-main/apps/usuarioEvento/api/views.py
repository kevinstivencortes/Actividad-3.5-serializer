from rest_framework.viewsets import ModelViewSet
from apps.usuarioEvento.api.serializers import UsuarioEventoSerializer
from apps.usuarioEvento.models import usuarioEvento
from apps.usuarioEvento.api.permissions import IsOwnerOrReadOnly

from apps.usuarioEvento.api.serializers import UsuarioEvento_registrar

""" lista y elimina """
class EventoViewSet(ModelViewSet):
    #permission_classes = [IsOwnerOrReadOnly]
    serializer_class = UsuarioEventoSerializer
    queryset = usuarioEvento.objects.all()
    http_method_names= ['get', 'delete']

""" egrega y actualiza """
class EventoRegistrar(ModelViewSet):
    serializer_class = UsuarioEvento_registrar
    queryset = usuarioEvento.objects.all()
    http_method_names= ['post', 'put']