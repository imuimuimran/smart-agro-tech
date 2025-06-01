from django.contrib import admin
from .models import Product
from .models import Service
from .models import ContactMessage
from .models import GalleryImage
from .models import Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = (
        'name', 'image',
        'feature1', 'feature2', 'feature3',
        'spec_label1', 'spec_value1',
        'spec_label2', 'spec_value2',
        'spec_label3', 'spec_value3',
        'spec_label4', 'spec_value4',
        'spec_label5', 'spec_value5',
        'spec_label6', 'spec_value6',
        'description',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Service)
admin.site.register(ContactMessage)
admin.site.register(GalleryImage)
admin.site.register(Order)
