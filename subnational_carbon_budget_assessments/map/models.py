from django.db import models
from .Data_preprocessing import get_data

class DataFile(models.Model):
    country = models.CharField(max_length=3, null=False)
    file = models.FileField(upload_to="data/")

    def __str__(self):
        return "%s" % (self.country)
    
    def save(self, *args, **kwargs):
        if not self.id:
            # TODO handle file and populate DB
            print(get_data(self.file, self.country, "1.5C").head)
        super(DataFile, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['country']

class Maps(models.Model):
    country = models.CharField(max_length=3, null=False)

    def __str__(self):
        return "%s" % (self.country)
    
    class Meta:
        ordering = ['country']

class States(models.Model):
    country = models.ForeignKey(Maps, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "%s" % (self.state)

    class Meta:
        ordering = ['country']

class Projections(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    data = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return "%s" % (self.data)
    
    class Meta:
        ordering = ['state']