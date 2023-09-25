from django.db import models


class Student(models.Model):
    WTID = models.IntegerField(help_text="WT ID")
    FirstName = models.CharField(max_length=30, help_text="First Name")
    LastName = models.CharField(max_length=30, help_text="Last Name")
    DegreeName = models.CharField(max_length=75, help_text="Degree Name")
    DegreeYear = models.IntegerField(help_text="Degree Year")
    TransferStudent = models.BooleanField(
        default=False, help_text="Transfer Student")
    CoursesCompleted = models.CharField(
        max_length=250, help_text="List of Courses Completed")

    def __str__(self):
        return self.name


class Degree(models.Model):
    DegreeName = models.CharField(max_length=75, help_text="Degree Name")
    DegreeYear = models.IntegerField(help_text="Degree Year")
    UniversityName = models.CharField(
        max_length=75, help_text="University Name")
    DepartmentName = models.CharField(
        max_length=75, help_text="Department Name")
    MajorName = models.CharField(max_length=75, help_text="Major Name")

    def __str__(self):
        return self.name


class Core_Requirements(models.Model):
    CourseID = models.CharField(max_length=10, help_text="Course ID")
    CourseName = models.CharField(max_length=50, help_text="Course Name")
    YearsRequired = models.IntegerField(help_text="List of Years Required")

    def __str__(self):
        return self.name


class University_Requirements(models.Model):
    UniversityName = models.CharField(
        max_length=50, help_text="University Name")
    CourseID = models.CharField(max_length=10, help_text="Course ID")
    CourseName = models.CharField(max_length=50, help_text="Course Name")
    YearsRequired = models.IntegerField(help_text="List of Years Required")

    def __str__(self):
        return self.name


class Department_Requirements(models.Model):
    DepartmentID = models.CharField(max_length=10, help_text="Department ID")
    DepartmentName = models.CharField(
        max_length=50, help_text="Department Name")
    CourseID = models.CharField(max_length=10, help_text="Course ID")
    CourseName = models.CharField(max_length=50, help_text="Course Name")
    YearsRequired = models.IntegerField(help_text="List of Years Required")

    def __str__(self):
        return self.name


class Major_Requirements(models.Model):
    MajorName = models.CharField(max_length=50, help_text="Major Name")
    CourseID = models.CharField(max_length=10, help_text="Course ID")
    CourseName = models.CharField(max_length=50, help_text="Course Name")
    YearsRequired = models.IntegerField(help_text="List of Years Required")

    def __str__(self):
        return self.name
