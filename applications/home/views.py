from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse
import json
from django.shortcuts import render
from django.http import HttpResponseForbidden

from yaml import Mark
from .models import Marker, Comment
import requests
from bs4 import BeautifulSoup
from .forms import Comment_form
from django.views.generic.edit import FormMixin
from django.db.models import Q
#from django.contrib.gis.geos import GEOSGeometry

"""def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")"""

#TODOS LOS ELEMENTOS

class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.all()
        context['comment'] = Comment.objects.all()[:8]
        return context

class PlanNatureView(TemplateView):
    template_name = "home/planNature.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.all()
        context['comment'] = Comment.objects.all()
        return context

class PlanCultureView(TemplateView):
    template_name = "home/planCulture.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.all()
        context['comment'] = Comment.objects.all()
        return context

class OpinionView(TemplateView):
    template_name = "home/opinion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.all()
        context['comment'] = Comment.objects.all()
        return context

class IndexView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class MapEuskadiView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class MapGipuzkoaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Gipuzkoa').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class MapBizkaiaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Bizkaia').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class MapArabaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Araba/Álava').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

#RESTAURANTES

class RestaurantesEuskadiView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(restorationType='Restaurante').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class RestaurantesGipuzkoaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Gipuzkoa',restorationType='Restaurante').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class RestaurantesBizkaiaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Bizkaia',restorationType='Restaurante').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class RestaurantesArabaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Araba/Álava',restorationType='Restaurante').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

#SIDRERIAS

class SidreriasEuskadiView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(restorationType='Sidreria').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class SidreriasGipuzkoaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Gipuzkoa',restorationType='Sidreria').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class SidreriasBizkaiaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Bizkaia',restorationType='Sidreria').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class SidreriasArabaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Araba/Álava',restorationType='Sidreria').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

#BODEGA TXAKOLI

class BodegaTxakoliEuskadiView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(restorationType='Bodega Txakoli').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class BodegaTxakoliGipuzkoaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Gipuzkoa',restorationType='Bodega Txakoli').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class BodegaTxakoliBizkaiaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Bizkaia',restorationType='Bodega Txakoli').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class BodegaTxakoliArabaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Araba/Álava',restorationType='Bodega Txakoli').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

#ASADOR TXAKOLI

class AsadorEuskadiView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(restorationType='Asador').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class AsadorGipuzkoaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Gipuzkoa',restorationType='Asador').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class AsadorBizkaiaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Bizkaia',restorationType='Asador').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

class AsadorArabaView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.filter(territory='Araba/Álava',restorationType='Asador').values('documentName','id','latwgs84','lonwgs84','restorationType')
        return context

#OTROS

"""class TableView(TemplateView):
    template_name = "home/table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.all()
        return context"""

class TableView(ListView):
    template_name = "home/table.html"
    model = Marker

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.all()
        return context"""

    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        print(name)
        if name:
            print(self)
            object_list = self.model.objects.filter(Q(documentName__icontains = name)|Q(locality__icontains = name)|Q(municipality__icontains = name)|Q(territory__icontains = name)|Q(postalCode__icontains = name)|Q(restorationType__icontains = name))
            print(object_list)
        else:
            print(self)
            object_list = self.model.objects.all()
            print(object_list)
        return object_list


#ENLACES
class LinkView(TemplateView):
    template_name = "home/enlaces.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Marker.objects.all()
        return context

class ContactView(TemplateView):
    template_name = "home/contactar.html"



#RESTAURANT DETAIL
class RestaurantDetailView(FormMixin, DetailView):
    model = Marker
    #context_object_name = 'restaurant'
    template_name = 'home/restaurantDetail.html'
    form_class = Comment_form

    def get_success_url(self):
        return reverse('restaurantDetail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rest = self.object
        form.save()
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Marker.objects.all()
        idFiltrar = self.object.id
        URL = Marker.objects.filter(id = idFiltrar).values('physicalUrl')
        URL1 = URL[0]
        URL2 = URL1['physicalUrl']
        page = requests.get(URL2)
        soup = BeautifulSoup(page.content, "html.parser")
        result = soup.find("div", class_="aa30_fichaBase_descripcion")
        result2 = result.text
        context['historia']=result2
        context['form'] = self.form_class()
        context['opinion'] = Comment.objects.filter(rest = self.object.id)

        imagesRest = []
        for img in soup.findAll('img'):
            imagenUrlText = img.get('src')
            #print(imagenUrlText)
            if '/contenidos/b_' in imagenUrlText:
                print(imagenUrlText)
                imagesRest.append(imagenUrlText)
                context['imageRest'] = imagenUrlText          
        print(imagesRest)
        context['imagesRest'] = imagesRest
        return context



def opendata(request):
    data = json.loads(json_string)
    print(data[0])

json_string = '''
{
  "documentName" : "Abeletxe",
  "documentDescription" : "El albergue-restaurante está en un paraje natural, y ofrece la calidad de un restaurante c...",
  "templateType" : "Restauración",
  "locality" : "Zizurkil",
  "qualityQ" : "",
  "qualityIconDescription" : "",
  "phone" : "943 693 983",
  "address" : "Zarate Bidea, s/n",
  "marks" : "Montes y Valles vascos",
  "physical" : "0",
  "visual" : "0",
  "auditive" : "0",
  "intellectual" : "0",
  "organic" : "0",
  "qualityAssurance" : "000001",
  "tourismEmail" : "info@abeletxe.com",
  "web" : "http://www.abeletxe.com/",
  "room" : "",
  "productClub" : "",
  "visit" : "",
  "capacity" : "000150",
  "store" : "",
  "postalCode" : "020159",
  "restorationType" : "Restaurante",
  "recomended" : "",
  "recomendedURLIcon" : "",
  "recomendedIconDescription" : "",
  "restaurant" : "000001",
  "bodega" : "000001",
  "michelinStar" : "",
  "repsolSun" : "",
  "latitudelongitude" : "43.200105403602,-2.0748274730163985",
  "latwgs84" : "43.200105403602",
  "lonwgs84" : "-2.0748274730163985",
  "municipality" : "Zizurkil",
  "municipalitycode" : "028",
  "territory" : "Gipuzkoa",
  "territorycode" : "000020",
  "country" : "España",
  "countrycode" : "000108",
  "friendlyUrl" : "https://turismoa.euskadi.eus/es/restaurantes/restaurante-abeletxe/aa30-12375/es/",
  "physicalUrl" : "https://turismoa.euskadi.eus/aa30-12375/es/contenidos/b_restauracion/0000046901_b1_rec_turismo/es_46901/46901-ficha2.html",
  "dataXML" : "https://turismoa.euskadi.eus/contenidos/b_restauracion/0000046901_b1_rec_turismo/es_46901/data/46901_openData.xml",
  "metadataXML" : "https://turismoa.euskadi.eus/contenidos/b_restauracion/0000046901_b1_rec_turismo/r01Index/0000046901_b1_rec_turismo-idxContent.xml",
  "zipFile" : "https://turismoa.euskadi.eus/contenidos/b_restauracion/0000046901_b1_rec_turismo/opendata/0000046901_b1_rec_turismo.zip"
}
'''


class MarcasView:
    def __init__(self, documentName, documentDescription, templateType, locality,qualityQ,qualityIconDescription,phone,address,marks,physical,visual,auditive,intellectual,organic,qualityAssurance,tourismEmail,web,room,productClub,visit,capacity,store,postalCode,restorationType,recomended,recomendedURLIcon,recomendedIconDescription,restaurant,bodega,michelinStar,repsolSun,latitudelongitude,latwgs84,lonwgs84,municipality,municipalitycode,territory,territorycode,country,countrycode,friendlyUrl,physicalUrl,dataXML,metadataXML,zipFile):
        self.documentName = documentName
        self.documentDescription = documentDescription
        self.templateType = templateType
        self.locality = locality
        self.qualityQ = qualityQ
        self.qualityIconDescription = qualityIconDescription
        self.phone = phone
        self.address = address
        self.marks = marks
        self.physical = physical
        self.visual = visual
        self.auditive = auditive
        self.intellectual = intellectual
        self.organic = organic
        self.qualityAssurance = qualityAssurance
        self.tourismEmail = tourismEmail
        self.web = web
        self.room = room
        self.productClub = productClub
        self.visit = visit
        self.capacity = capacity
        self.store = store
        self.postalCode = postalCode
        self.restorationType = restorationType
        self.recomended = recomended
        self.recomendedURLIcon = recomendedURLIcon
        self.recomendedIconDescription = recomendedIconDescription
        self.restaurant = restaurant
        self.bodega = bodega
        self.michelinStar = michelinStar
        self.repsolSun = repsolSun
        self.latitudelongitude = latitudelongitude
        self.latwgs84 = latwgs84
        self.lonwgs84 = lonwgs84
        self.municipality = municipality
        self.municipalitycode = municipalitycode
        self.territory = territory
        self.territorycode = territorycode
        self.country = country
        self.countrycode = countrycode
        self.friendlyUrl = friendlyUrl
        self.physicalUrl = physicalUrl
        self.dataXML = dataXML
        self.metadataXML = metadataXML
        self.zipFile = zipFile    

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return f'<MarcasView { self.documentName }>'

json_string = '''{
  "documentName" : "Abeletxe",
  "documentDescription" : "El albergue-restaurante está en un paraje natural, y ofrece la calidad de un restaurante c...",
  "templateType" : "Restauración",
  "locality" : "Zizurkil",
  }'''

def insertarDatos(request):
    users_list = []
    with open('restaurantes.json', 'r') as json_file:
        user_data = json.loads(json_file.read())
        for u in user_data:
            #users_list.append(MarcasView(**u))
            marca = Marker()
            marca.documentName = (u['documentName'])
            marca.documentDescription = (u['documentDescription'])
            marca.templateType = (u['templateType'])
            marca.locality = (u['locality'])
            marca.qualityQ = (u['qualityQ'])
            marca.qualityIconDescription = (u['qualityIconDescription'])
            marca.phone = (u['phone'])
            marca.address = (u['address'])
            marca.marks = (u['marks'])
            marca.physical = (u['physical'])
            marca.visual = (u['visual'])
            marca.auditive = (u['auditive'])
            marca.intellectual = (u['intellectual'])
            marca.organic = (u['organic'])
            marca.qualityAssurance = (u['qualityAssurance'])
            marca.tourismEmail = (u['tourismEmail'])
            marca.web = (u['web'])
            marca.room = (u['room'])
            marca.productClub = (u['productClub'])
            marca.visit = (u['visit'])
            marca.capacity = (u['capacity'])
            marca.store = (u['store'])
            marca.postalCode = (u['postalCode'])
            marca.restorationType = (u['restorationType'])
            marca.recomended = (u['recomended'])
            marca.recomendedURLIcon = (u['recomendedURLIcon'])
            marca.recomendedIconDescription = (u['recomendedIconDescription'])
            marca.restaurant = (u['restaurant'])
            marca.bodega = (u['bodega'])
            marca.michelinStar = (u['michelinStar'])
            marca.repsolSun = (u['repsolSun'])
            marca.latitudelongitude = (u['latitudelongitude'])
            marca.latwgs84 = (u['latwgs84'])
            marca.lonwgs84 = (u['lonwgs84'])
            marca.municipality = (u['municipality'])
            marca.municipalitycode = (u['municipalitycode'])
            marca.territory = (u['territory'])
            marca.country = (u['country'])
            marca.countrycode = (u['countrycode'])
            marca.friendlyUrl = (u['friendlyUrl'])
            marca.physicalUrl = (u['physicalUrl'])
            marca.dataXML = (u['dataXML'])
            marca.metadataXML = (u['metadataXML'])
            marca.zipFile = (u['zipFile'])
            marca.save()

def insertarParques(request):
    users_list = []
    with open('espacios-naturales.json', 'r') as json_file3:
        user_data3 = json.load(json_file3)
        print(user_data3)
        for u in user_data3:
            print(u[0])
       
           

    #print(users_list)

def post_detailview(request, id):
  if request.method == 'POST':
    cf = Comment(request.POST or None)
    if cf.is_valid():
      content = request.POST.get('content')
      comment = Comment.objects.create(post = Marker, user = request.user, content = content)
      comment.save()
      return redirect(Marker.get_absolute_url())
    else:
      cf = comment_form()
        
    context ={
      'comment_form':cf,
      }
    return render(request, 'socio/_detail.html', context)

