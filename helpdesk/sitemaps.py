from django.contrib.sitemaps import Sitemap
from .models import KBItem

class KBEntrySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return KBItem.objects.all()

    def lastmod(self, obj):
        return obj.last_updated



