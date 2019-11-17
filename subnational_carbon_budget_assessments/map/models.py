from django.db import models

class Maps(models.Model):
    country = models.CharField(max_length=255, null=False)

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