from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('edit', views.edit),
    path('users/<int:userid>', views.users),
    path('addfavoritequote', views.addfavoritequote),
    path('success/<int:quoteid>/delete', views.deletequote),
    path('edit/<int:userid>/update', views.updateuserinfo)
]


# path('edit/<int:quoteid>', views.edit),




#     path('show', views.displayshows),     # URL TO SHOW LIST OF SHOWS #
#     path('show/new', views.index),          # URL TO ADD A NEW SHOW #
#     path('show/create', views.createshow),  # CREATE NEW SHOW#
#    	path('show/info/<int:showid>', views.showinfo),
#    	path('show/edit/<int:showid>', views.editshow),
#    	path('show/delete/<int:showid>', views.deleteshow),
#    	path('show/update/<int:showid>', views.updateshow),
# ]
