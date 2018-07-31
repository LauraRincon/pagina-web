from import_export import resources
from .models import Boya

class BoyaResource(resources.ModelResource):
    class Meta:
        model = Boya
