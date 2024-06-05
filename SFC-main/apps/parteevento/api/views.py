from rest_framework.viewsets import ModelViewSet
from apps.parteevento.api.serializers import ParteEventoSerializer
from apps.parteevento.models import ParteEvento
""" registrar y actualizar  """
from apps.parteevento.api.serializers import ParteEvento_por_id

class ParteEvento_registrar(ModelViewSet):
    serializer_class = ParteEvento_por_id
    queryset = ParteEvento.objects.all()
    http_method_names= ['post', 'put', 'get']


""" listar y eliminar """
class ParteEventoViewSet(ModelViewSet):
    serializer_class = ParteEventoSerializer
    queryset = ParteEvento.objects.all()
    http_method_names= ['get', 'delete']