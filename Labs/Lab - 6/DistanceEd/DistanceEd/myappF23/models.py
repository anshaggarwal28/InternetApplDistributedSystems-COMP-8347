from django.db import models

# Student Model
# Defines the Student model.
class Student(models.Model):
    STUDENT_STATUS_CHOICES = [
        ('ER', 'Enrolled'),
        ('SP', 'Suspended'),
        ('GD', 'Graduated'),
    ]
    # Fields of the Student model.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Unique email for student
    date_of_birth = models.DateField()
    status = models.CharField(max_length=2, choices=STUDENT_STATUS_CHOICES, default='ER')

    # String representation of the Student model.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Instructor Model
# Defines the Instructor model.
class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()  # Bio for instructor
    students = models.ManyToManyField(Student, blank=True)  # ManyToMany relationship with students

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Category Model
# Defines the Category model.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Course Model
# Defines the Course model.
class Course(models.Model):
    COURSE_LEVEL_CHOICES = [
        ('BE', 'Beginner'),
        ('IN', 'Intermediate'),
        ('AD', 'Advanced'),
    ]
    # Fields of the Course model.
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="courses")  # One-to-many relationship with Instructor
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)  # Corrected typo and added on_delete constraint
    students = models.ManyToManyField(Student, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.CharField(max_length=2, choices=COURSE_LEVEL_CHOICES, default='BE')  # Course level with choices

    def __str__(self):
        return self.title


# order model

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        (0, 'Order Confirmed'),
        (1, 'Order Cancelled'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=1)
    order_date = models.DateField()

    def __str__(self):
        return f"Order {self.id} - {self.student} - {self.course}"
