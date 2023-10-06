from django.urls import path
from . import views, adminViews

urlpatterns = [
    path('', views.home),
    path('assignments/', views.assignments),
    path('classes/', views.classes),
    path('classes/<int:classname>/', views.classSite),
    path('classes/<int:classname>/assignments', views.classSiteAssignments),
    path('classes/<int:classname>/gradebook', views.classSiteAssignments),
    path('classes/<int:classname>/messages', views.ClassMessages),
    path('classes/<int:classname>/messages/create', views.sendMessage),
    path('messages', views.allMessages),
    path('profile/<str:username>', views.profile),
    path('profile/', views.profile),

    path('admin/', adminViews.admin),
    path('admin/<int:classname>/', adminViews.classAdmin),
    path('admin/<int:classname>/assignments/', adminViews.assignments),
    path('admin/<int:classname>/assignments/create/', adminViews.createAssignment),
    path('admin/<int:classname>/gradebook/', adminViews.admin),

]
# MAKE MESSAGES
#messages can be viewed on the messahes screen, but to make one you have to go to the class site