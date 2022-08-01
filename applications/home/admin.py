from django.contrib import admin
from django.contrib.gis import admin
from .models import Marker, Comment, NaturalPark


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("id","documentName", "name", "location")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author","rest", "text", "date","qualityPrice")

@admin.register(NaturalPark)
class NaturalParkAdmin(admin.ModelAdmin):
    list_display = ("id","documentName")
