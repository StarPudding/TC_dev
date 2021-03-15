from django.db import models


class monitor_list(models.Model):
    monitor_id = models.CharField(max_length=8)
    monitor_name = models.CharField(max_length=100)
    monitor_url = models.CharField(max_length=100)
    monitor_parameter = models.CharField(max_length=100)
    monitor_belong = models.CharField(max_length=100)
    last_offline_date = models.DateField

    class Meta:
        db_table = 'monitor_list'
