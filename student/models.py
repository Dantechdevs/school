from django.db import models
from django.utils.text import slugify

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_mobile = models.CharField(max_length=15)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_mobile = models.CharField(max_length=15)
    mother_email = models.EmailField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)  # Ensure student_id is unique
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=20, unique=True)  # Ensure admission_number is unique
    section = models.CharField(max_length=10)
    student_image = models.ImageField(default="default.jpg", upload_to="student_images")
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
            slug = base_slug
            counter = 1
            while Student.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class Notification(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming you're using Django's built-in User model
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:20]}..."
