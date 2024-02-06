from django.db import models

class aggregation(models.Model):
    aggregated_date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f"Aggregation on {self.aggregated_date}"