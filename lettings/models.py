from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


# Create your models here.
class Address(models.Model):
    """
    Represents an address with a number, street, city,
    state, zip code, and country ISO code.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
        This class contains metadata options for the Address model.
        """

        verbose_name_plural = "Addresses"  # Correct pluralization here

    def __str__(self):
        """
        Returns a string representation of the object.
        The string representation consists of the number and
        street of the property.
        Returns:
        str: The string representation of the object.
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a letting in the system.
    Attributes:
        title (str): The title of the letting.
        address (Address): The address of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return self.title
