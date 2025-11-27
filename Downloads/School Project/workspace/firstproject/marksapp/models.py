# marksapp/models.py

from django.db import models

class Session(models.Model):
    session = models.CharField(max_length=9)
    def __str__(self): return self.session

class ClassSection(models.Model):
    class_name = models.CharField(max_length=10)
    section = models.CharField(max_length=5)
    def __str__(self): return f"{self.class_name} - {self.section}"

class Subject(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): return self.name

class Student(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100, blank=True)
    mothers_name = models.CharField(max_length=100, blank=True)
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    def __str__(self): return f"{self.roll_no} - {self.name}"

# Scholastic Marks
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    pt1 = models.IntegerField(default=0)
    notebook_t1 = models.IntegerField(default=0)
    sub_enrich_t1 = models.IntegerField(default=0)
    half_yearly = models.IntegerField(default=0)
    pt2 = models.IntegerField(default=0)
    notebook_t2 = models.IntegerField(default=0)
    sub_enrich_t2 = models.IntegerField(default=0)
    annual = models.IntegerField(default=0)

    def term1_total(self): return self.pt1 + self.notebook_t1 + self.sub_enrich_t1 + self.half_yearly
    def term2_total(self): return self.pt2 + self.notebook_t2 + self.sub_enrich_t2 + self.annual
    def final_total(self): return round((self.term1_total() + self.term2_total()) / 2, 1)

# Co-Scholastic & Discipline
class CoScholasticActivity(models.Model):
    CATEGORY_CHOICES = [
        ('2A', 'Part 2(A): Co-Scholastic Activities(To be assessed on a 3 point scale)'),
        ('2B', 'Part 2(B): Health & Physical Education (To be assessed on a 3 point scale)'),
        ('3',  'Part 3: Discipline')
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.get_category_display()} - {self.name}"
    

# Grades of student for each activity
class CoScholasticGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.ForeignKey(CoScholasticActivity, on_delete=models.CASCADE)

    term1_grade = models.CharField(
        max_length=1,
        choices=[('A','A'),('B','B'),('C','C')],
        default='B'
    )
    term2_grade = models.CharField(
        max_length=1,
        choices=[('A','A'),('B','B'),('C','C')],
        default='B'
    )

    class Meta:
        unique_together = ('student', 'activity')   # ✔ SAME ACTIVITY duplicate na ho

    def __str__(self):
        return f"{self.student.name} - {self.activity.name}"