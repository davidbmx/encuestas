import os
import uuid
from PIL import Image

from django.conf import settings

def uglifyImageName(instance, filename, ruc = None):
    extension = filename.split('.')[-1]
    if instance != None:
        pk = instance.ruc
    else:
        pk = ruc

    if extension == 'p12':
        ruta = 'firmas'
    else:
        ruta = 'logotipos'
        
    return '{}/{}/{}.{}'.format(ruta, pk, uuid.uuid4(), extension)

def uglifyImageNameEst(instance, filename, ruc = None):
    extension = filename.split('.')[-1]
    if instance != None:
        pk = instance.empresa.ruc
    else:
        pk = ruc

    return 'logotipos/{}/establecimiento/{}.{}'.format(pk, uuid.uuid4(), extension)


def create_thumb(file, thumbnail_size=(256, 256)):
    image = Image.open(file)
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)
    array_data = file.name.split(".")
    extension = array_data.pop()
    basename = ''.join(array_data)
    filename = '{}_thumb.{}'.format(basename, extension)
    image.save(os.path.join(settings.MEDIA_ROOT,filename))
    return filename

class ManageFiles:

    def get_object(self):
        return self.queryset
    def get_fieldimage(self):
        return self.fieldimage
    def get_fieldthumb(self):
        return self.fieldthumb

    def create_thumb(self):
        queryset = self.get_object()
        fieldimage = self.get_fieldimage()
        fieldthumb = self.get_fieldthumb()
        image = Image.open(queryset.__dict__[fieldimage])
        image.thumbnail(thumbnail_size, Image.ANTIALIAS)
        array_data = queryset.__dict__[fieldimage].name.split(".")
        extension = array_data.pop()
        basename = ''.join(array_data)
        filename = '{}_thumb.{}'.format(basename, extension)
        image.save(os.path.join(settings.MEDIA_ROOT,filename))
        queryset.__dict__[fieldthumb] = filename
        queryset.save()
