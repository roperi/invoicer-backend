from django.urls import path
from .views import FeatureList, BenefitList, HeroSectionView, PricingPlanListView, ItemListView

urlpatterns = [
    path('features/', FeatureList.as_view(), name='feature_list'),
    path('benefits/', BenefitList.as_view(), name='benefit_list'),
    path('hero/', HeroSectionView.as_view(), name='hero-section'),
    path('pricing-plans/', PricingPlanListView.as_view(), name='pricing-plan-list'),
    path('items/', ItemListView.as_view(), name='item_list'),
]
