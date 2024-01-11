from django.contrib import admin
from .models import FeatureSection, BenefitSection, HeroSection, PricingPlan, Item


class FeatureSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'icon')
    search_fields = ('title', 'description')


admin.site.register(FeatureSection, FeatureSectionAdmin)


class BenefitSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'icon')
    search_fields = ('title', 'description')


admin.site.register(BenefitSection, BenefitSectionAdmin)


class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('headline', 'subheadline')
    search_fields = ('headline', )


admin.site.register(HeroSection, HeroSectionAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Item, ItemAdmin)


class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'monthly_cost')
    filter_horizontal = ('items',)


admin.site.register(PricingPlan, PricingPlanAdmin)
