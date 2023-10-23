from django.shortcuts import render
from .models import (Student, Degree, Core_Requirements,
                     University_Requirements, Department_Requirements,
                     Major_Requirements)
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from .forms import (StudentForm, DegreeForm, CoreForm,
                    UniForm, DepForm, MajForm)


# Create your views here.


def student_list(request):
    context = {}
    context["student_list"] = Student.objects.all().order_by('WTID').values()

    return render(request, 'degree_checklist/student_list.html', context)


def degree_list(request):
    context = {}
    context["degree_list"] = Degree.objects.all().order_by(
        'DegreeName').values()

    return render(request, 'degree_checklist/degree_list.html', context)


def core_requirement_list(request):
    context = {}
    context["core_requirement_list"] = Core_Requirements.objects.all().order_by(
        'CoreCourseID').values()

    return render(request, 'degree_checklist/core_requirement_list.html', context)


def university_requirement_list(request):
    context = {}
    context["university_requirement_list"] = University_Requirements.objects.all(
    ).order_by('UniversityName', 'UniCourseID').values()

    return render(request, 'degree_checklist/university_requirement_list.html', context)


def department_requirements_list(request):
    context = {}
    context["department_requirements_list"] = Department_Requirements.objects.all(
    ).order_by('DepartmentID', 'DepartmentName', 'DepCourseID').values()

    return render(request, 'degree_checklist/department_requirements_list.html', context)


def major_requirements_list(request):
    context = {}
    context["major_requirements_list"] = Major_Requirements.objects.all().order_by(
        'MajorName', 'MajCourseID').values()

    return render(request, 'degree_checklist/major_requirements_list.html', context)


class StudentRecordFormView(FormView):
    template_name = 'student_form.html'
    form_class = StudentForm
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DegreeRecordFormView(FormView):
    template_name = 'degree_form.html'
    form_class = DegreeForm
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CoreRecordFormView(FormView):
    template_name = 'core_form.html'
    form_class = CoreForm
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UniRecordFormView(FormView):
    template_name = 'uni_form.html'
    form_class = UniForm
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DepRecordFormView(FormView):
    template_name = 'department_form.html'
    form_class = DepForm
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MajRecordFormView(FormView):
    template_name = 'major_form.html'
    form_class = MajForm
    success_url = 'entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Record saved successfully.")
