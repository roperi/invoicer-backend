from django.db import models


class HeroSection(models.Model):
    headline = models.CharField(max_length=255)
    subheadline = models.CharField(max_length=255)

    def __str__(self):
        return self.headline


class FeatureSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class BenefitSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PricingPlan(models.Model):
    title = models.CharField(max_length=255)
    monthly_cost = models.DecimalField(max_digits=8, decimal_places=2)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.title
