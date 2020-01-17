from django.contrib.postgres.fields import CIEmailField
from django.db import models
from typing_extensions import final


@final
class Consent(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"


@final
class LegalBasis(models.Model):
    """
    Main model for querying about legal basis, the primary key is
    an email address. You can see this to find the consent types an
    email address has consented to.
    """

    email = CIEmailField(primary_key=True)

    consents = models.ManyToManyField(Consent)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """All django models should have this method."""
        return f"{self.email}"
