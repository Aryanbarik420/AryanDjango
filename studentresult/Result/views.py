from django.shortcuts import render

# Create your views here.
from Result.models import Marks

def home(request):
    response=render(request,"Result/index.html")
    return response

def add_student_template(request):
    return render(request,"Result/add_student.html")

def add_student(request):
    rno=int(request.GET['rno'])
    name=request.GET['name']
    s1=float(request.GET['s1'])
    s2=float(request.GET['s2'])

    data=Marks(Rollno=rno,Name=name,Sub1=s1,Sub2=s2)
    data.save()

    response=render(request,"Result/add_student.html",context={'msg':'Student added'})
    return response 


def update_student_template(request):
    return render(request,"Result/update_student.html")


def update_student(request):
    rno=int(request.GET['rno'])
    s1=float(request.GET['s1'])
    s2=float(request.GET['s2'])
    rows_updated = Marks.objects.filter(Rollno=rno).update(Sub1=s1, Sub2=s2)
    if rows_updated:
        msg = "Marks Updated"
    else:
        msg = "Invalid Rollno"
    response = render(request, "Result/update_student.html", context={'msg': msg})
    return response


def delete_student_template(request):
    return render(request,"Result/delete_student.html")

def delete_student(request):
    rno=int(request.GET['rno'])
    row_delete=Marks.objects.filter(Rollno=rno).delete()
    if row_delete:
        msg = "Student deleted"
    else:
        msg = "Invalid Rollno"
    response=render(request,"Result/delete_student.html",context={'msg':msg})
    return response



def find_result_template(request):
    return render(request,"Result/find_result.html")


def find_result(request):
    rno = int(request.GET['rno'])
    try:
        data=Marks.objects.get(Rollno=rno)
        result="PASS" if data.Sub1 >= 33 and data.Sub2 >= 33 else "FAIL"
        return render(request,"Result/show_result.html",context={'result':result,'data':data})
    except:
        return render(request,"Result/find_result.html",context={'msg':'Invalid Rollno'})

def view_student(request):
    qs=Marks.objects.all()
    return render(request,"Result/view_student.html",context={'qs':qs})