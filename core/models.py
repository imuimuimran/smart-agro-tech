from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField(blank=True)
    
    # Add feature points
    feature1 = models.CharField(max_length=255, blank=True)
    feature2 = models.CharField(max_length=255, blank=True)
    feature3 = models.CharField(max_length=255, blank=True)
    
    # Dynamic spec labels and values
    spec_label1 = models.CharField(max_length=100, blank=True)
    spec_value1 = models.CharField(max_length=255, blank=True)

    spec_label2 = models.CharField(max_length=100, blank=True)
    spec_value2 = models.CharField(max_length=255, blank=True)

    spec_label3 = models.CharField(max_length=100, blank=True)
    spec_value3 = models.CharField(max_length=255, blank=True)

    spec_label4 = models.CharField(max_length=100, blank=True)
    spec_value4 = models.CharField(max_length=255, blank=True)

    spec_label5 = models.CharField(max_length=100, blank=True)
    spec_value5 = models.CharField(max_length=255, blank=True)

    spec_label6 = models.CharField(max_length=100, blank=True)
    spec_value6 = models.CharField(max_length=255, blank=True)

    

    def __str__(self):
        return self.name
    

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)  # Optional for icons like FontAwesome

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=14)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title or f"Image {self.id}"


class Order(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=14)
    email = models.EmailField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.name} ({self.mobile})"