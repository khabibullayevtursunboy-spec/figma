from django.db import models
from django.contrib.auth.models import User


class Massage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    text = models.TextField(verbose_name="Matn / Xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"

    def __str__(self):
        return self.text


class Birinchisahifa(models.Model):
    kattamatn = models.CharField(max_length=800, verbose_name="Katta matn (Sarlavha)")
    kichikmatn = models.TextField(verbose_name="Kichik matn (Tavsif)")
    yuklashmatni = models.CharField(max_length=200, verbose_name="Yuklash tugmasi matni")

    class Meta:
        verbose_name = "Bosh sahifa matni"
        verbose_name_plural = "Bosh sahifa matnlari"

    def __str__(self):
        return self.kattamatn


class Appdownload(models.Model):
    platform_name = models.CharField(max_length=200, verbose_name="Platforma nomi")
    platform_url = models.URLField(verbose_name="Platforma havolasi (URL)")

    class Meta:
        verbose_name = "Ilova yuklash havolasi"
        verbose_name_plural = "Ilova yuklash havolalari"


class TeamMember(models.Model):
    avatar = models.ImageField(upload_to='team_avatars/', verbose_name="Rasmi (Avatar)")

    class Meta:
        verbose_name = "Jamoa a'zosi"
        verbose_name_plural = "Jamoa a'olari"

    def __str__(self):
        return f"A'zo {self.id}"


class Feature(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")

    class Meta:
        verbose_name = "Afzallik (Feature)"
        verbose_name_plural = "Afzalliklar (Features)"

    def __str__(self):
        return self.title


class TeamGroup(models.Model):
    title = models.CharField(max_length=100, verbose_name="Guruh nomi")
    members_count = models.PositiveIntegerField(default=0, verbose_name="A'zolar soni")
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name="Rang kodi")

    class Meta:
        verbose_name = "Jamoa guruhi"
        verbose_name_plural = "Jamoa guruhlari"

    def __str__(self):
        return self.title


class TeamSectionFeature(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")

    class Meta:
        verbose_name = "Jamoa bo'limi xususiyati"
        verbose_name_plural = "Jamoa bo'limi xususiyatlari"

    def __str__(self):
        return self.title


class HowItWorksStep(models.Model):
    step_number = models.PositiveIntegerField(unique=True, verbose_name="Qadam raqami")
    title = models.CharField(max_length=200, verbose_name="Qadam sarlavhasi")
    description = models.TextField(verbose_name="Qadam tavsifi")

    class Meta:
        ordering = ['step_number']
        verbose_name = "Qanday ishlaydi qadami"
        verbose_name_plural = "Qanday ishlaydi qadamlari"

    def __str__(self):
        return f"{self.step_number}. {self.title}"


class VideoSection(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="Video sarlavhasi")
    cover_image = models.ImageField(upload_to='video_covers/', verbose_name="Ustki rasm (Poster)")
    video_url = models.URLField(verbose_name="Video havolasi (URL)")

    class Meta:
        verbose_name = "Video bo'limi"
        verbose_name_plural = "Video bo'limlari"

    def __str__(self):
        return self.title or f"Video {self.id}"


class AppProblemSolution(models.Model):
    icon = models.ImageField(upload_to='solutions_icons/', blank=True, null=True, verbose_name="Ikonka / Rasm")
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")

    class Meta:
        verbose_name = "Muammo yechimi (Xizmat)"
        verbose_name_plural = "Muammo yechimlari (Xizmatlar)"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    author_name = models.CharField(max_length=100, verbose_name="Muallif ismi")
    author_avatar = models.ImageField(upload_to='testimonials_avatars/', verbose_name="Muallif rasmi")
    comment = models.TextField(verbose_name="Fikr / Izoh matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = "Mijoz fikri"
        verbose_name_plural = "Mijozlar fikrlari"

    def __str__(self):
        return self.author_name


class PricingPlan(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tarif nomi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    billing_period = models.CharField(max_length=20, default="/ mo", verbose_name="To'lov davri (masalan: / oylik)")

    team_members = models.CharField(max_length=100, verbose_name="Jamoa a'zolari cheklovi")
    cloud_storage = models.CharField(max_length=100, verbose_name="Bulutli xotira haajmi")
    meetings = models.CharField(max_length=100, verbose_name="Uchrashuvlar / Majlislar")
    support = models.CharField(max_length=100, verbose_name="Qo'llab-quvvatlash xizmati")

    is_popular = models.BooleanField(default=False, verbose_name="Ommabop tarif sifatida ko'rsatish")

    class Meta:
        verbose_name = "Tarif rejasi"
        verbose_name_plural = "Tarif rejalari"

    def __str__(self):
        return self.name


class FooterLink(models.Model):
    CATEGORY_CHOICES = [
        ('company', 'Kompaniya'),
        ('product', 'Mahsulot'),
        ('legal', 'Hujjatlar'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Kategoriya")
    title = models.CharField(max_length=100, verbose_name="Havola nomi")
    url = models.CharField(max_length=255, default="#", verbose_name="Havola manzili (URL)")

    class Meta:
        verbose_name = "Futering havolasi"
        verbose_name_plural = "Futer havolalari"

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"


class FooterSettings(models.Model):
    app_store_url = models.URLField(default="https://apple.com", verbose_name="App Store havolasi")
    google_play_url = models.URLField(default="https://google.com", verbose_name="Google Play havolasi")
    copyright_text = models.CharField(max_length=255, default="© 2026 Copyright, All Right Reserved", verbose_name="Mualliflik huquqi matni")

    twitter_url = models.URLField(blank=True, null=True, verbose_name="Twitter havolasi")
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Facebook havolasi")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Instagram havolasi")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn havolasi")

    class Meta:
        verbose_name = "Futer sozlamasi"
        verbose_name_plural = "Futer sozlamalari"

    def __str__(self):
        return "Futer sozlamalari"