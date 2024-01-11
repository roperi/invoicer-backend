from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FeatureSection, BenefitSection, HeroSection, Item, PricingPlan
from .serializers import (FeatureSerializer, BenefitSerializer, HeroSectionSerializer, PricingPlanSerializer,
                          ItemSerializer)


class FeatureList(APIView):

    def get(self, request):
        features = FeatureSection.objects.all()
        serializer = FeatureSerializer(features, many=True)
        return Response(serializer.data)


class BenefitList(APIView):

    def get(self, request):
        benefits = BenefitSection.objects.all()
        serializer = BenefitSerializer(benefits, many=True)
        return Response(serializer.data)


class HeroSectionView(generics.ListAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PricingPlanListView(generics.ListAPIView):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer
