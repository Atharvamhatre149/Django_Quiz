from django.contrib import admin
from django.urls import path
from Quiz import views
urlpatterns = [
    path("", views.home,name='home'),
    path("signin",views.signin,name='signin'),
    path("signup",views.signup,name='signup'),
    path("signout",views.signout,name='signout'),
    path("python",views.python,name='python'),
    path("aoa",views.aoa,name='aoa'),
    path("dbms",views.dbms,name='dbms'),
    path("os",views.os,name='os'),
    path("Quizselect",views.Quizselect,name='Quizselect'),
    path("score",views.score,name="score"),
    path("showScore",views.showScore,name="showScore")
]
