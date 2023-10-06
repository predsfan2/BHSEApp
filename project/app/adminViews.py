from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import CreateAssignment
from .models import Assignment


@login_required
def admin(request):
    return render(request, "admin.html",
                  {"user": request.user, "classes": request.user.profile.classes_as_teacher.all()})


@login_required
def classAdmin(request, classname):
    # checks if the user has permission to acces
    if request.user.profile.classes_as_teacher.filter(id=classname):
        return render(request, "admin/classes.html", {"user": request.user, "classname": classname})
    else:
        return HttpResponseRedirect("/admin")


def assignments(request, classname):
    if request.user.profile.isTeacher or request.user.is_superuser or request.user.is_staff:
        g
    else:
        return HttpResponseRedirect("/")


def createAssignment(request, classname):
    if request.method == "POST":
        form = CreateAssignment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/admin")
    else:
        form = CreateAssignment()
    return render(request, "admin/createAssignment.html", {"form": form})
