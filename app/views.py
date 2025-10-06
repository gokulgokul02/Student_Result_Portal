from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from app.models import Results, Users ,Notification

def home(request):
    notify=Notification.objects.order_by('-created_at')
    context = {"notify":notify}
    if request.method == 'POST':
        reg_no = request.POST.get("reg_no")
        dob = request.POST.get("dob")

        try:
            # Get exact user
            user_details = Users.objects.get(reg_no=reg_no, dob=dob)
            print("SUCCESS")

            # Get results for that user
            results = Results.objects.filter(Users=user_details)  # Use `Users` since your field is named like that
            context['results'] = results
            context['user'] = user_details

        except ObjectDoesNotExist:
            print("YOU FIRST REGISTER AND THEN COME")
            context['error'] = "NOT REGISTERED"
    
    return render(request, "index.html", context)


def admin(request):
    return render(request,"overview.html")

def overview(request):
    users_count=Users.objects.count()
    results_count=Results.objects.count()
    notifications_count=Notification.objects.count()
    return render(request,"overview.html",{"users_count":users_count,"results_count":results_count,"notifications_count":notifications_count})
def add_student(request):
    if request.method=='POST':
        name=request.POST.get('name')
        reg_no=request.POST.get('reg_no')
        year_of_study=request.POST.get('year_of_study')
        department=request.POST.get('department')
        clg_name=request.POST.get('clg_name')
        university_name=request.POST.get('university_name')
        dob=request.POST.get('dob')
        add=Users(name=name,reg_no=reg_no,year_of_Study=year_of_study,department=department,  clg_name=clg_name,university_name=university_name,dob=dob)
        add.save()
        return redirect('users')
    return render(request,"add_student.html")

def users(request):
    users=Users.objects.all()
    return render(request,"users.html",{"users":users})
def add_result(request):
    result=Results.objects.all()
    users = Users.objects.all()
    if request.method == 'POST':
        user_id = request.POST.get('user')  # get the selected user id from the form
        result_file = request.FILES.get('result')
        
        # Get the actual user object
        user = Users.objects.get(id=user_id)
        
        # Save the result
        add_result = Results(Users=user, result=result_file)  # user is the ForeignKey field
        add_result.save()
    
    return render(request, "add_result.html", {"users": users,"result":result})



def post_notification(request):
    return render(request,"post_notification.html")


def edit_student(request,id):
    edit=get_object_or_404(Users,id=id)
    if request.method=='POST':
        edit.name=request.POST.get('name')
        edit.reg_no=request.POST.get('reg_no')
        edit.year_of_Study=request.POST.get('year_of_study')
        edit.department=request.POST.get('department')
        edit.clg_name=request.POST.get('clg_name')
        edit.university_name=request.POST.get('university_name')
        edit.dob=request.POST.get('dob')
        edit.save()
        return redirect('users')
    return render(request,"edit_student.html",{"edit":edit})


def delete_student(request,id):
    delete_user=get_object_or_404(Users,id=id)
    delete_user.delete()
    return redirect('users')


from django.shortcuts import render, get_object_or_404, redirect
from app.models import Results, Users

from django.shortcuts import render, get_object_or_404, redirect
from app.models import Results, Users

def edit_result(request, id):
    edit_result = get_object_or_404(Results, id=id)

    if request.method == 'POST':
        user_name = request.POST.get('user')  # Get the name from text input

        # Assign user
        try:
            user_instance = Users.objects.get(name=user_name)
            edit_result.user = user_instance
        except Users.DoesNotExist:
            error = f"No user found with name '{user_name}'"
            return render(request, "edit_result.html", {"edit_result": edit_result, "error": error})

        # Assign file only if a new one is uploaded
        if 'result' in request.FILES:
            edit_result.result = request.FILES['result']

        edit_result.save()
        return redirect('add_result')

    return render(request, "edit_result.html", {"edit_result": edit_result})


def delete_result(request,id):
    delete_result=get_object_or_404(Results,id=id)
    delete_result.delete()
    return redirect('add_result')


def view_result(request, id):
    results = Results.objects.filter(Users=id)
   
    return render(request,'view_result.html',{"results":results})


def post_notification(request):
    notify=Notification.objects.all()
    if request.method=="POST":
        message=request.POST.get('message')

        notification=Notification(Message=message)
        notification.save()
       
    return render(request,"post_notification.html",{"notify":notify})


def edit_notification(request,id):
    edit_notification=get_object_or_404(Notification,id=id)
    if request.method=='POST':
        edit_notification.Message=request.POST.get('message')
        edit_notification.save()
        return redirect('post_notification')
    return render(request,"edit_notification.html",{"edit_notification":edit_notification})

def delete_notification(request,id):
    edit_notification=get_object_or_404(Notification,id=id)
    edit_notification.delete()
    
    return redirect('post_notification')