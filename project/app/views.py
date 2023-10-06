from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader

from .forms import CreateMessage
from .models import Profile, Assignment, ClassSites, Message

def GetClassMessages(class_id):
    class_messages = Message.objects.filter(classAssignedTo_id=class_id)
    return class_messages

@login_required
def home(request):
    user_classes = ClassSites.objects.filter(students=request.user.profile)
    assignments = Assignment.objects.filter(classAssignedTo__in=user_classes, classAssignedTo__isnull=False)
    messages = request.user.messages.all()
    return render(request, "home.html", {"profile": request.user, 'assignments': assignments, 'messages': messages})


@login_required
def assignments(request):
    user_classes = ClassSites.objects.filter(students=request.user.profile)
    assignments = Assignment.objects.filter(classAssignedTo__in=user_classes, classAssignedTo__isnull=False)

    return render(request, "assignments.html", {'assignments': assignments})


@login_required
def classes(request):
    return render(request, "classes.html", {"user": request.user, "classes": request.user.profile.classes_as_student.all()})


@login_required
def classSite(request, classname):
    return render(request, "classsite.html")


@login_required
def classSiteAssignments(request, classname):
    return render(request, "classsite.html")


def profile(request, username=None):
    if username is None:
        profile = request.user.profile
    else:
        profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'profile.html', {'profile': profile})


def sendMessage(request, classname):
    if request.method == 'POST':
        form = CreateMessage(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.classAssignedTo_id = classname
            message.save()
            form.save_m2m()
            redirUrl = '/classes/' + str(classname) + '/messages'
            return redirect(redirUrl, class_id=classname)
    else:
        form = CreateMessage()

    return render(request, 'createMessage.html', {'form': form, 'class_site': classname})


def ClassMessages(request, classname):
    messages = GetClassMessages(classname)
    return render(request, 'messages.html', {'class_site': classname, 'messages': messages})


def allMessages(request):
    messages = request.user.messages.all()
    return render(request, 'messages.html', {'messages': messages})