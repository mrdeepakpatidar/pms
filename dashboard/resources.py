from import_export import resources
from .models import Lic,Lead,Mutual_Fund

class LicResource(resources.ModelResource):
    class Meta:
        model = Lic



class LeadResource(resources.ModelResource):
    class Meta:
        model = Lead


class FundResource(resources.ModelResource):
    class Meta:
        model = Mutual_Fund