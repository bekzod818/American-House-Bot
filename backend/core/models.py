from django.db import models


class User(models.Model):
    tg_id = models.PositiveBigIntegerField(verbose_name='User ID', unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    age = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "Users"

    def __str__(self) -> str:
        return str(self.tg_id)


class Coupon(models.Model):
    image_url = models.URLField(verbose_name="Kupon rasmi uchun link")
    text = models.TextField(max_length=1024, verbose_name="Rasmdan keyingi matn")

    class Meta:
        db_table = "Coupon"

    def __str__(self) -> str:
        return "Kupon"


class Chance(models.Model):
    image_url = models.URLField(verbose_name="Imkoniyatlar rasmi uchun link")
    text = models.TextField(max_length=1024, verbose_name="Rasmdan keyingi matn")

    class Meta:
        db_table = "Chance"

    def __str__(self) -> str:
        return "Imkoniyatlar"


class About(models.Model):
    data = (
        ('univer', 'Universitet'),
        ('house', 'American House')
    )
    telegraph = models.URLField(verbose_name="Telegraph/YouTube uchun link", null=True)
    image_url = models.URLField(verbose_name="Rasm uchun link", null=True)
    text = models.TextField(max_length=1024, verbose_name="Rasmdan keyingi matn")
    type = models.CharField(max_length=10, choices=data)

    class Meta:
        db_table = "About"

    def __str__(self) -> str:
        return self.type


class Fakultet(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    slug = models.SlugField(max_length=255, unique=True)
    image_url = models.URLField(verbose_name="Rasm uchun link")
    text = models.TextField(max_length=1024, verbose_name="Rasmdan keyingi matn")
    profile = models.URLField(verbose_name="Bog'lanish uchun")

    class Meta:
        verbose_name = "Fakultet"
        verbose_name_plural = "Fakultetlar"
        db_table = "Fakultet"

    def __str__(self) -> str:
        return self.name
