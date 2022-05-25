from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from datetime import datetime, timedelta
from collections import Counter
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect('admin_home')
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            users = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
            request.session['u_id'] = users
            request.session['username'] = users.fullname
            request.session['u_id'] = users.id
            users = user_registration.objects.filter(id=users.id)
            return render(request, 'user_home.html', {'users': users})
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        u = user_registration()
        u.fullname = request.POST['name']
        u.username = request.POST['username']
        u.email = request.POST['email']
        u.password = request.POST['password']
        u.joiningdate = datetime.now()
        u.save()
        return render(request, 'login.html')
    return render(request, 'register.html')

# ============ Admin Module ======================


def admin_logout(request):
    if 'Adm_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


def admin_index(request):
    return render(request, 'admin_index.html')


def admin_home(request):
    user = user_registration.objects.count()
    sub = subject.objects.count()
    exam = exams.objects.count()
    quest = questions.objects.count()
    return render(request, 'admin_home.html', {'user': user, 'sub': sub, 'exam': exam, 'quest': quest})


def admin_user(request):
    user = user_registration.objects.all()
    return render(request, 'admin_user.html', {'user': user})


def admin_add_exam(request, id):
    sub = subject.objects.get(id=id)
    if request.method == 'POST':
        a = exams()
        sub = subject.objects.get(id=id)
        a.subject = sub
        a.examname = request.POST['en']
        a.examdescription = request.POST['ed']
        a.save()
        return redirect('admin_exam')
    return render(request, 'admin_exams_adding.html', {'sub': sub})


def admin_add_subject(request):
    sub = subject.objects.all().order_by('-id')
    return render(request, 'admin_add_subject.html', {'sub': sub})


def admin_sub_add(request):
    if request.method == 'POST':
        a = subject()
        a.subjectname = request.POST['sn']
        a.subjectdescription = request.POST['desc']
        a.save()
        return redirect('admin_add_subject')
    return render(request, 'admin_sub_add.html')


def admin_deletesub(request, id):
    data = subject.objects.get(id=id)
    data.delete()
    return redirect('admin_add_subject')


def admin_exams_adding(request, id):
    sub = subject.objects.get(id=id)
    return render(request, 'admin_exams_adding.html', {'sub': sub})


def admin_exam(request):
    exam = exams.objects.all().order_by('-id')
    return render(request, 'admin_exam.html', {'exam': exam})


def admin_add_questions(request, id):
    exam = exams.objects.get(id=id)
    if request.method == 'POST':
        a = questions()
        ex = exams.objects.get(id=id)
        a.question = request.POST['q']
        a.option1 = request.POST['o1']
        a.option2 = request.POST['o2']
        a.option3 = request.POST['o3']
        a.option4 = request.POST['o4']
        a.answer = request.POST['o4']
        a.exam = ex
        a.save()
        return redirect('admin_exam')
    return render(request, 'admin_add_questions.html', {'exam': exam})


def admin_view_questions(request, id):
    q = questions.objects.filter(exam_id=id)
    return render(request, 'admin_view_questions.html', {'q': q})


def admin_exam_delete(request, id):
    e = exams.objects.get(id=id)
    e.delete()
    return redirect('admin_exam')


def admin_question_delete(request, id):
    q = questions.objects.get(id=id)
    q.delete()
    return redirect('admin_exam')


# ============ User Module ======================
def user_logout(request):
    if 'u_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


def user_index(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']
    users = user_registration.objects.filter(id=u_id)
    return render(request, 'user_index.html', {'users': users})


def user_home(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']
    users = user_registration.objects.filter(id=u_id)
    return render(request, 'user_home.html', {'users': users})


def user_subject(request):
    if 'u_id' in request.session:
        if request.session.has_key('u_id'):
            u_id = request.session['u_id']
        else:
            variable = "dummy"
        users = user_registration.objects.filter(id=u_id)
    sub = subject.objects.all()
    return render(request, 'user_subject.html', {'users': users, 'sub': sub})


def user_exam(request, id):
    if 'u_id' in request.session:
        if request.session.has_key('u_id'):
            u_id = request.session['u_id']
        else:
            variable = "dummy"
        users = user_registration.objects.filter(id=u_id)
    ex = exams.objects.filter(subject_id=id)
    return render(request, 'user_exam.html', {'users': users, 'ex': ex})


def user_exam_attend(request, id):
    if 'u_id' in request.session:
        if request.session.has_key('u_id'):
            u_id = request.session['u_id']
        else:
            variable = "dummy"
        users = user_registration.objects.filter(id=u_id)
    # q=questions.objects.filter(exam_id=id)
    qus = questions.objects.filter(exam_id=id).order_by('?')[:3]
    if request.method == "POST":
        for q in qus:
            print(request.POST.get(q.question))
            print("id:", q.id)
            print("ans:", q.answer)
            c = 0
            if q.answer == request.POST.get(q.question):
                c += 1
        print("mark:", c)
        return redirect('user_subject')
    return render(request, 'user_exam_attend.html', {'users': users, 'q': qus, })


def user_answer(request):
    if request.session.has_key('u_id'):
        u_id = request.session['u_id']

    users = user_registration.objects.filter(id=u_id)
    qus = questions.objects.all()
    for q in qus:
        print(request.POST.get(q.question))
        print(q.id)
    return redirect('user_subject')
