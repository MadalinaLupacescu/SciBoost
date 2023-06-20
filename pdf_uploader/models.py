'''
from django.db import models


class PubMedRecord(models.Model):
    record_id = models.CharField(max_length=255)
    article_identifier = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    affiliation = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    publication_date = models.CharField(max_length=255, null=True, blank=True)
    publication_type = models.CharField(max_length=255, null=True, blank=True)
    location_identifier = models.CharField(max_length=255, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    drug_entities = models.TextField(null=True, blank=True)
    ade_entities = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"PubMedRecord {self.record_id}"
'''
from django.db import models

class PubMedRecord(models.Model):
    record_id = models.IntegerField(primary_key=True)
    article_identifier = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    affiliation = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    publication_date = models.CharField(max_length=255, null=True)
    publication_type = models.CharField(max_length=255, null=True)
    location_identifier = models.CharField(max_length=255, null=True)
    abstract = models.TextField(null=True)
    drug_entities = models.TextField(null=True, blank=True)
    ade_entities = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"PubMedRecord {self.record_id}"


