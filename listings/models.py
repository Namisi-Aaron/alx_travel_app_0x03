from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    """
    Model representing a user in the travel application.
    Each user can host listings and make bookings.
    """
    user_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    email = models.EmailField(unique=True, null=False)
    password_hash = models.CharField(max_length=128, null=False)
    role = models.CharField(choices=[
        ('host', 'Host'),
        ('guest', 'Guest')
    ], max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        ordering = ['-created_at']
    
    objects = models.Manager()

class Listing(models.Model):
    """
    Model representing a property listing in the travel application.
    Each listing is associated with a host (user)
    and contains details about the listing.
    """
    listing_id = models.IntegerField(primary_key=True, editable=False)
    host_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='listings'
    )
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    location = models.CharField(max_length=255, null=False)
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'listing'
        verbose_name = 'Listing'
        ordering = ['-created_at']
    
    objects = models.Manager()

class Booking(models.Model):
    """Model representing a booking made by a user for a listing.
    Each booking is associated with a listing and a user.
    """
    booking_id = models.IntegerField(primary_key=True, editable=False)
    listing_id = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='bookings')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled')
    ], default='pending', null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'''
        Booking for {self.listing_id.title} by {self.user_id.first_name} {self.user_id.last_name}
        '''

    class Meta:
        db_table = 'booking'
        verbose_name = 'Booking'
        ordering = ['-created_at']
        unique_together = ('listing_id', 'user_id', 'start_date', 'end_date')
    
    objects = models.Manager()

class Review(models.Model):
    """
    Model representing a review left by a user about a listing.
    Each review is associated with a listing and a user.
    """
    review_id = models.IntegerField(primary_key=True, editable=False)
    listing_id = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='reviews')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], null=False)
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'''
        Review for {self.listing_id.title} by {self.user_id.first_name} {self.user_id.last_name}
        Rating: {self.rating}
        Comment: {self.comment}
        '''
    
    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        ordering = ['-created_at']
    
    objects = models.Manager()

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True, editable=False)
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='payments')
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ], default='pending', null=False)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    transaction_id = models.CharField(max_length=255, null=False)
