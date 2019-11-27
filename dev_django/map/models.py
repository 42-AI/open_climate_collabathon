from django.db import models
from .Data_preprocessing import get_data
from django.core.exceptions import ValidationError

def populate_db(country, data):
    new_map, _ = Maps.objects.update_or_create(country=country)
    new_map.save()
    data.drop(["Total"], inplace=True)
    for regionName in data.index.values:
        new_regionName, _ = States.objects.update_or_create(country=Maps.objects.get(country=country), regionName=regionName)
        new_regionName.save()
        new_serie, _ = Series.objects.update_or_create(regionName=new_regionName, serie="Population of %s" % regionName)
        new_serie.save()
        years = data.columns
        for year, data_pt in enumerate(data.loc[regionName, :]):
            new_point, _ = Points.objects.update_or_create(serie=new_serie, year=years[year], data=data_pt)
            new_point.save()

class DataFile(models.Model):
    country = models.CharField(max_length=3, null=False, unique=True)
    file = models.FileField(upload_to="data/")

    def __str__(self):
        return "%s" % (self.country)
    
    def save(self, *args, **kwargs):
        if not self.id:
            # TODO handle file and populate DB
            data = get_data(data_file=self.file, country=self.country, scenario="1.5C")
            if len(data) > 0:
                populate_db(self.country, data)
        super(DataFile, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['country']

class Maps(models.Model):
    country = models.CharField(max_length=3, null=False, unique=True)

    def __str__(self):
        return "%s" % (self.country)
    
    class Meta:
        ordering = ['country']

class States(models.Model):
    country = models.ForeignKey(Maps, on_delete=models.CASCADE)
    regionName = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "%s" % (self.regionName)

    class Meta:
        ordering = ['country']

class Series(models.Model):
    regionName = models.ForeignKey(States, on_delete=models.CASCADE)
    serie = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return "%s" % (self.serie)
    
    class Meta:
        ordering = ['regionName']

class Points(models.Model):
    serie = models.ForeignKey(Series, on_delete=models.CASCADE)
    year = models.IntegerField(null=False)
    data = models.FloatField(null=True)
    
    def __str__(self):
        return "%d: %s" % (self.year, self.data)
    
    class Meta:
        ordering = ['serie', 'year']