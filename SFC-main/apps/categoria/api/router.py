from rest_framework.routers import DefaultRouter

from apps.categoria.api.views import CategoriaViewSet

from apps.categoria.api.views import Categoria_listar



router_categoria = DefaultRouter()
router_categoria.register(prefix='categoria', basename='categoria', viewset=CategoriaViewSet)

router_categoria.register(prefix='categoriaRegist', basename='categoriaRegist', viewset=Categoria_listar)