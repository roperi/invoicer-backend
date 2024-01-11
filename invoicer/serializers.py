from rest_framework import serializers
from .models import FeatureSection, BenefitSection, HeroSection, Item, PricingPlan


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureSection
        fields = ['id', 'title', 'description', 'icon']


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenefitSection
        fields = ['id', 'title', 'description', 'icon']


class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = ['headline', 'subheadline']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']


class PricingPlanSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = PricingPlan
        fields = ['id', 'title', 'monthly_cost', 'items']

