from rest_framework.viewsets import ModelViewSet
from apps.categoria.api.serializers import CategoriaSerializer
from apps.categoria.models import Categoria

""" registrar y actualizar """
from apps.categoria.api.serializers import Categoria_por_id

class Categoria_listar(ModelViewSet):
    serializer_class = Categoria_por_id
    queryset = Categoria.objects.all()
    http_method_names= ['post', 'put']


""" listar y eliminar """
class CategoriaViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    http_method_names= ['get', 'delete']