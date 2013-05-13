from django.contrib import admin
from carousel.models import Carousel, CarouselElement


class CarouselElementInline(admin.TabularInline):
    model = CarouselElement


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    inlines = [CarouselElementInline]

admin.site.register(Carousel, CarouselAdmin)
