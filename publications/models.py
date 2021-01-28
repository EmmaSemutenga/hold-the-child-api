from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    DOCUMENT_TYPES = (
        ('Ethics', 'Ethics'),
        ('Standards', 'Standards'),
        ('Policies', 'Policies'),
        ('Memos', 'Memos'),
        ('Manual', 'Manual'),
    )
    document_type = models.CharField(max_length=100, blank=True, null=True, choices = DOCUMENT_TYPES)
    publication_date = models.DateField(blank=True, null=True)
    name_of_publisher = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title
