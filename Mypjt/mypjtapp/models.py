from django.db import models
from sre_parse import Verbose
from multiselectfield import MultiSelectField


class DistrictModel(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class BranchModel(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    district = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)


class DetailsModel(models.Model):
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    account_choices = (
        ('savings', 'Savings'),
        ('current', 'Current')
    )
    material_choices = (
        ('cb', 'Cheque book'),
        ('debit', 'Debit'),
        ('credit', 'Credit')
    )

    Name = models.CharField(max_length=40, null=False)
    Date_Of_Birth = models.DateField(auto_now_add=True, null=False, blank=False)
    Gender = models.BooleanField(default=False, choices=gender_choices, blank=False)
    Contact_Number = models.CharField(max_length=40, blank=False, null=False)
    district = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
    branch = models.ForeignKey(BranchModel, on_delete=models.CASCADE)
    Account_Type = models.BooleanField(default=False, choices=account_choices, blank=False)

    Materials = MultiSelectField(choices=material_choices, max_choices=3,
                                 max_length=30)

    def __str__(self):
        return '{}'.format(self.Name)
