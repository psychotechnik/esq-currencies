#import os
#from django.db import models

#def filepath(instance, filename):
#	return os.path.join("uploads/%s/%s/%s" %(instance._meta.module_name, instance.pk, filename))
#class Attachment(models.Model):
#    name = models.CharField(max_length=255)
#    description = models.TextField()
#    file = models.FileField(upload_to=filepath)
#    def __unicode__(self):
#        return self.name




