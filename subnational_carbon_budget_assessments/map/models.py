from django.db import models
from .Data_preprocessing import get_data
from django.core.exceptions import ValidationError

def populate_db(country, data):
    new_map, _ = Maps.objects.update_or_create(country=country)
    new_map.save()
    for state in data.index.values:
        new_state, _ = States.objects.update_or_create(country=Maps.objects.get(country=country), state=state)
        new_state.save()
        #new_proj, _ = Projections.objects.update_or_create(state=new_state, data=data.loc[state])
        #new_proj.save()


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