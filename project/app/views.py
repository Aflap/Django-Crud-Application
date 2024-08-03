from django.shortcuts import render,get_object_or_404
from .models import Category,Student



# Create your views here.
def student_list(request):
    
    categories=Category.objects.all()
    category_id=request.GET.get('category')
    if category_id:
        students=Student.objects.filter(category_id=category_id)
    else:
        students=Student.objects.all()
    return render(request,"student_list.html",{'students':students,'categories':categories})

def category_students(request,category_id):
    category=get_object_or_404(category,id=category_id)
    students=Student.objects.filter(category=category)
    categories=Category.objects.all()
    return render(request,"student_list.html",{'students':students,'categories':categories})

