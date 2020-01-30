from django.db import models


# class OfficeRoom(models.Model):
#
#     number = models.CharField(max_length=256, blank=True, null=True, default=None)
#     floor = models.IntegerField(default=0, null=True, blank=True)
#     building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return "(id.%s) - %s" % (self.id, self.title)
