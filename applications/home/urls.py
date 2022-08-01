from django.urls import path
from django.views.generic import TemplateView
from .views import IndexView, ContactView, LinkView, insertarDatos, insertarParques, opendata, MarcasView, RestaurantDetailView, TableView, LinkView, MapGipuzkoaView, MapBizkaiaView, MapArabaView, RestaurantesEuskadiView, RestaurantesGipuzkoaView, RestaurantesBizkaiaView, RestaurantesArabaView, SidreriasEuskadiView, SidreriasGipuzkoaView, SidreriasBizkaiaView, SidreriasArabaView, BodegaTxakoliEuskadiView, BodegaTxakoliGipuzkoaView, BodegaTxakoliBizkaiaView, BodegaTxakoliArabaView, AsadorEuskadiView, AsadorGipuzkoaView, AsadorBizkaiaView, AsadorArabaView, HomeView, MapEuskadiView, PlanNatureView, PlanCultureView, OpinionView
from . import views
#from djgeojson.views import GeoJSONLayerView
import json

urlpatterns = [
    #path('', views.index, name='index'),
    #Todos los elementos
    path('', HomeView.as_view(), name='index'),
    path('mapEuskadi', MapEuskadiView.as_view(), name='mapEuskadi'),
    path('mapGipuzkoa', MapGipuzkoaView.as_view(), name='mapGipuzkoa'),
    path('mapBizkaia', MapBizkaiaView.as_view(), name='mapBizkaia'),
    path('mapAraba', MapArabaView.as_view(), name='mapAraba'),
    #Restaurantes
    path('restaurantesEuskadi', RestaurantesEuskadiView.as_view(), name='restaurantesEuskadi'),
    path('restaurantesGipuzkoa', RestaurantesGipuzkoaView.as_view(), name='restaurantesGipuzkoa'),
    path('restaurantesBizkaia', RestaurantesBizkaiaView.as_view(), name='restaurantesBizkaia'),
    path('restaurantesAraba', RestaurantesArabaView.as_view(), name='restaurantesAraba'),
    #Sidrerias
    path('sidreriasEuskadi', SidreriasEuskadiView.as_view(), name='sidreriasEuskadi'),
    path('sidreriasGipuzkoa', SidreriasGipuzkoaView.as_view(), name='sidreriasGipuzkoa'),
    path('sidreriasBizkaia', SidreriasBizkaiaView.as_view(), name='sidreriasBizkaia'),
    path('sidreriasAraba', SidreriasArabaView.as_view(), name='sidreriasAraba'),
    #Bodega Txakoli
    path('bodegaTxakoliEuskadi', BodegaTxakoliEuskadiView.as_view(), name='bodegaTxakoliEuskadi'),
    path('bodegaTxakoliGipuzkoa', BodegaTxakoliGipuzkoaView.as_view(), name='bodegaTxakoliGipuzkoa'),
    path('bodegaTxakoliBizkaia', BodegaTxakoliBizkaiaView.as_view(), name='bodegaTxakoliBizkaia'),
    path('bodegaTxakoliAraba', BodegaTxakoliArabaView.as_view(), name='bodegaTxakoliAraba'),
    #Asador
    path('asadorEuskadi', AsadorEuskadiView.as_view(), name='asadorEuskadi'),
    path('asadorGipuzkoa', AsadorGipuzkoaView.as_view(), name='asadorGipuzkoa'),
    path('asadorBizkaia', AsadorBizkaiaView.as_view(), name='asadorBizkaia'),
    path('asadorAraba', AsadorArabaView.as_view(), name='asadorAraba'),

    path('contact/', ContactView.as_view(), name='contactar'),
    path('enlaces/', LinkView.as_view(), name='enlaces'),
    path('opendata/', opendata),
    path('marcas/', MarcasView),
    path('insertarDatos/', insertarDatos),
    path('restaurantDetail/<int:pk>/', RestaurantDetailView.as_view(), name='restaurantDetail'),
    path('table/', TableView.as_view(), name='table'),
    path('insertarParques/', insertarParques),

    path('planNature/', PlanNatureView.as_view(), name='planNature'),
    path('planCulture/', PlanCultureView.as_view(), name='planCulture'),
    path('opinion/', OpinionView.as_view(), name='opinion'),
    #Buscador
    #path('buscador/', busqueda, name='busqueda'),

]