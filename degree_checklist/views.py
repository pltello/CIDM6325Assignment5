from django.shortcuts import render
from .models import (Student, Degree, Core_Requirements,
                     University_Requirements, Department_Requirements,
                     Major_Requirements)


# Create your views here.


def student_list(request):
    context = {}
    context["student_list"] = Student.objects.all()

    return render(request, 'degree_checklist/student_list.html', context)


def degree_list(request):
    context = {}
    context["degree_list"] = Degree.objects.all()

    return render(request, 'degree_checklist/degree_list.html', context)


def core_requirement_list(request):
    context = {}
    context["core_requirement_list"] = Core_Requirements.objects.all()

    return render(request, 'degree_checklist/core_requirement_list.html', context)


def university_requirement_list(request):
    context = {}
    context["university_requirement_list"] = University_Requirements.objects.all()

    return render(request, 'degree_checklist/university_requirement_list.html', context)


def department_requirements_list(request):
    context = {}
    context["department_requirements_list"] = Department_Requirements.objects.all()

    return render(request, 'degree_checklist/department_requirements_list.html', context)


def major_requirements_list(request):
    context = {}
    context["major_requirements_list"] = Major_Requirements.objects.all()

    return render(request, 'degree_checklist/major_requirements_list.html', context)
