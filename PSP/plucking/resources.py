from import_export import resources

from .models import Resources


class ExcellRead(resources.ModelResource):

    class Meta:
        model = Resources