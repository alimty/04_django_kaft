from django.db import models

DEFAULT_SATATUS = "darft"


STATUS = [
    # left side : DB
    # right side: human-readable name
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),

]


class Page(models.Model):
    page_name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(
      default=DEFAULT_SATATUS,
      choices=STATUS,
      max_length=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
