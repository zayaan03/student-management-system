from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import csv
from .models import Student
from .forms import StudentForm

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    form = StudentForm()
    return render(request, 'students/list.html', {
        'students': students,
        'form': form,
        'show_add_modal': False,
    })

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        students = Student.objects.all()
        return render(request, 'students/list.html', {
            'students': students,
            'form': form,
            'show_add_modal': True,
        })

    students = Student.objects.all()
    form = StudentForm()
    return render(request, 'students/list.html', {
        'students': students,
        'form': form,
        'show_add_modal': True,
    })

def student_edit_form(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    return render(request, 'students/edit_form_partial.html', {'form': form, 'student': student})

def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        students = Student.objects.all()
        return render(request, 'students/list.html', {
            'students': students,
            'form': form,
            'show_edit_modal': True,
            'edit_student_id': id,
        })
    
    form = StudentForm(instance=student)
    students = Student.objects.all()
    return render(request, 'students/list.html', {
        'students': students,
        'form': form,
        'show_edit_modal': True,
        'edit_student_id': id,
    })

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return redirect('student_list')
    
    return render(request, 'students/delete.html', {'student': student})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Dispostion'] = 'attachment; filename = "students.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Student ID',
         'Name',
         'Email',
         'Department',
         'Semester',
         'CGPA'
        ]

    )
    students = Student.objects.all()
    for student in students:
        writer.writerow(
            [student.student_id,
             student.name,
             student.email,
             student.department,
             student.semester,
             student.cgpa
            ]
        )
    return response

def export_txt(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = "students.txt"'

    students = Student.objects.all()
    for student in students:
        response.write(f'Student ID: {student.student_id}\n'
                       f'Name: {student.name}\n'
                       f'Email: {student.email}\n'
                       f'Department: {student.department}\n'
                       f'Semester: {student.semester}\n'
                       f'CGPA: {student.cgpa}\n========================================\n'
                       
                       )
    return response