from rest_framework.parsers import MultiPartParser
import ipdb

# Create your models here.
class File(MultiPartParser):
    media_type = 'text/plain'
