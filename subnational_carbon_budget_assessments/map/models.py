from django.db import models

def handle_file(instance, filename):
    # TODO handle file content
    return "data/%s" % filename

class DataFile(models.Model):
    title = models.CharField(max_length=50, null=False)
    file = models.FileField(upload_to=handle_file)

    def __str__(self):
        return "%s" % (self.title)
    
    class Meta:
        ordering = ['title']

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