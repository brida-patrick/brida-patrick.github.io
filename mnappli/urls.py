from django.urls import path
from .import views


app_name = 'mnappli'

urlpatterns = [
    path('',views.index,name='index' ),
     
     path('<int:book_id>/',views.show,name='show'),
     path('ajout-livre/',views.add,name='add'),
     path('modifier/<int:book_id>/',views.edith,name='edith'),
     path('remove/<int:book_id>/',views.remove,name='remove'),
     path('heure/',views.heure,name='heure')
    
]
