from django.contrib import admin
from .models import DistrictModel, BranchModel, DetailsModel
# Register your models here.

admin.site.register(DistrictModel)
admin.site.register(BranchModel)
admin.site.register(DetailsModel)
