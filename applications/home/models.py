from django.db import models
from django.contrib.gis.db import models
from rest_framework_gis import serializers
from django.contrib.auth.models import User
import datetime

class Marker(models.Model):
    """A marker with name and location."""
    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    documentName = models.CharField(max_length=255, null=True, blank=True)
    documentDescription = models.CharField(max_length=255, null=True, blank=True)
    templateType = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    qualityQ = models.CharField(max_length=255, null=True, blank=True)
    qualityIconDescription = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    marks = models.CharField(max_length=255, null=True, blank=True)
    physical = models.CharField(max_length=255, null=True, blank=True)
    visual = models.CharField(max_length=255, null=True, blank=True)
    auditive = models.CharField(max_length=255, null=True, blank=True)
    intellectual = models.CharField(max_length=255, null=True, blank=True)
    organic = models.CharField(max_length=255, null=True, blank=True)
    qualityAssurance = models.CharField(max_length=255, null=True, blank=True)
    tourismEmail = models.CharField(max_length=255, null=True, blank=True)
    web = models.CharField(max_length=255, null=True, blank=True)
    room = models.CharField(max_length=255, null=True, blank=True)
    productClub = models.CharField(max_length=255, null=True, blank=True)
    visit = models.CharField(max_length=255, null=True, blank=True)
    capacity = models.CharField(max_length=255, null=True, blank=True)
    store = models.CharField(max_length=255, null=True, blank=True)
    postalCode = models.CharField(max_length=255, null=True, blank=True)
    restorationType = models.CharField(max_length=255, null=True, blank=True)
    recomended = models.CharField(max_length=255, null=True, blank=True)
    recomendedURLIcon = models.CharField(max_length=255, null=True, blank=True)
    recomendedIconDescription = models.CharField(max_length=255, null=True, blank=True)
    restaurant = models.CharField(max_length=255, null=True, blank=True)
    bodega = models.CharField(max_length=255, null=True, blank=True)
    michelinStar = models.CharField(max_length=255, null=True, blank=True)
    repsolSun = models.CharField(max_length=255, null=True, blank=True)
    latitudelongitude = models.CharField(max_length=255, null=True, blank=True)
    latwgs84 = models.CharField(max_length=255, null=True, blank=True)
    lonwgs84 = models.CharField(max_length=255, null=True, blank=True)
    municipality = models.CharField(max_length=255, null=True, blank=True)
    municipalitycode = models.CharField(max_length=255, null=True, blank=True)
    territory = models.CharField(max_length=255, null=True, blank=True)
    territorycode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    countrycode = models.CharField(max_length=255, null=True, blank=True)
    friendlyUrl = models.CharField(max_length=255, null=True, blank=True)
    physicalUrl = models.CharField(max_length=255, null=True, blank=True)
    dataXML = models.CharField(max_length=255, null=True, blank=True)
    metadataXML = models.CharField(max_length=255, null=True, blank=True)
    zipFile = models.CharField(max_length=255, null=True, blank=True)
    #_num = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        """Return string representation."""
        return self.documentName

class MarkerSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        fields = ("id", "name")
        geo_fields = "location"
        model = Marker

class Comment(models.Model):
    QUALITY_PRICE = [
        (1, 'Mal / Gaizki'),
        (2, 'Suficiente / Nahikoa'),
        (3, 'Bien / Ondo'),
        (4, 'Muy bien / Oso ondo'),
        (5, 'Excelente / Bikain'),
    ]

    SERVICE = [
        (1, 'Mal / Gaizki'),
        (2, 'Suficiente / Nahikoa'),
        (3, 'Bien / Ondo'),
        (4, 'Muy bien / Oso ondo'),
        (5, 'Excelente / Bikain'),
    ]

    FOOD = [
        (1, 'Mal / Gaizki'),
        (2, 'Suficiente / Nahikoa'),
        (3, 'Bien / Ondo'),
        (4, 'Muy bien / Oso ondo'),
        (5, 'Excelente / Bikain'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rest = models.ForeignKey(Marker, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    complementNaturePlan = models.TextField(max_length=500, null=True, blank=True)
    complementCulturePlan = models.TextField(max_length=500, null=True, blank=True)
    complementOtherPlan = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    qualityPrice = models.IntegerField(
        choices=QUALITY_PRICE,
        default=3,
    )
    service = models.IntegerField(
        choices=SERVICE,
        default=3,
    )
    food = models.IntegerField(
        choices=FOOD,
        default=3,
    )

    

    def __str__(self):
        return self.text



class NaturalPark(models.Model):
    documentName = models.CharField(max_length=255, null=True, blank=True)
    documentDescription = models.CharField(max_length=255, null=True, blank=True)
    templateType = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    qualityQ = models.CharField(max_length=255, null=True, blank=True)
    qualityIconDescription = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    marks = models.CharField(max_length=255, null=True, blank=True)
    physical = models.CharField(max_length=255, null=True, blank=True)
    visual = models.CharField(max_length=255, null=True, blank=True)
    auditive = models.CharField(max_length=255, null=True, blank=True)
    intellectual = models.CharField(max_length=255, null=True, blank=True)
    organic = models.CharField(max_length=255, null=True, blank=True)
    tourismEmail = models.CharField(max_length=255, null=True, blank=True)
    web = models.CharField(max_length=255, null=True, blank=True)
    natureType = models.CharField(max_length=255, null=True, blank=True)
    latitudelongitude = models.CharField(max_length=255, null=True, blank=True)
    latwgs84 = models.CharField(max_length=255, null=True, blank=True)
    lonwgs84 = models.CharField(max_length=255, null=True, blank=True)
    municipality = models.CharField(max_length=255, null=True, blank=True)
    municipalitycode = models.CharField(max_length=255, null=True, blank=True)
    territory = models.CharField(max_length=255, null=True, blank=True)
    territorycode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    countrycode = models.CharField(max_length=255, null=True, blank=True)
    friendlyUrl = models.CharField(max_length=255, null=True, blank=True)
    physicalUrl = models.CharField(max_length=255, null=True, blank=True)
    dataXML = models.CharField(max_length=255, null=True, blank=True)
    metadataXML = models.CharField(max_length=255, null=True, blank=True)
    zipFile  = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.documentName

