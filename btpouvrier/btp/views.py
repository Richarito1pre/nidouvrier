from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile, Post,LikePost
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from itertools import chain
#from .forms import ProfileForm
from django.db import models
from django.utils import timezone
from django.utils import timezone


# Create your views here.

#@login_required(login_url='signin')
def index(request):
    #user_object = User.objects.get(username=request.user.username)
    #user_profile = Profile.objects.get(user=user_object)
    return render(request,'index.html')

def liste_ouvriers(request):
    #user_object = User.objects.get(username=request.user.username)
    #user_profile = Profile.objects.get(user=user_object)
    return render(request,'liste_ouvriers.html')



from datetime import datetime, time

from django.shortcuts import render

from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from datetime import datetime

@login_required(login_url='signin')
def home(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()
    
    liked_posts = LikePost.objects.filter(username=request.user.username).values_list('post_id', flat=True)
    formatted_posts = []
    for post in posts:
        formatted_date = post.date_travo.strftime('%d/%m/%Y')
        formatted_post = {
            'post': post,
            'formatted_date': formatted_date
        }
        formatted_posts.append(formatted_post)
    
    context = {
        'user_profile': user_profile,
        'formatted_posts': formatted_posts,
        'liked_posts': liked_posts,
    }

    return render(request, 'home.html', context)


from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_date(value):
    if isinstance(value, datetime):
        return value.strftime('%d/%m/%Y')
    return value


    return render(request, 'home.html', context)


def addanonce(request):
    return render(request,'addanonce.html')



def acceuil(request):
    return render(request,'autre/acceuil.html')
def ouvrier(request):
    return render(request,'ouvrier.html')
def ouvrier_detail(request):
    return render(request,'ouvrier_detail.html')
def param(request):
    return render(request,'autre/param.html')
def inscrip(request):
    return render(request,'autre/inscrip.html')
def compte(request):
    return render(request,'autre/compte.html')
def connexion(request):
    return render(request,'autre/connexion.html')

def ouvriers(request):
    return render(request,'ouvriers.html')
from django.shortcuts import render

def base(request):
    # Votre logique de vue ici
    # ...

    context = {
        'request': request,
        # Autres variables de contexte si nécessaire
    }

    return render(request, 'base.html', context)

def mesanonces(request):
    return render(request,'mesannonces.html')

#def favoris(request):
    #return render(request,'favoris.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email deja existant')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'nom deja existant')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Mot de pass trop court')
            return redirect('signup')
        
    else:
        return render(request,'signup.html') 


def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('settings')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'login.html')
#-----debut parametre du compte

#@login_required(login_url='signin')
@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        
        if request.FILES.get('profile_picture') == None:
            profile_picture  = user_profile.profile_picture 
            first_name  = request.POST['first_name']
            last_name  = request.POST['last_name']
            address  = request.POST['address']
            group = request.POST['group']
            specialty  = request.POST['specialty']
            phone_number  = request.POST['phone_number']

            user_profile.profile_picture  = profile_picture 
            user_profile.first_name  = first_name 
            user_profile.last_name  =  last_name 
            user_profile.address= address
            user_profile.group = group
            user_profile.specialty = specialty
            user_profile.phone_number = phone_number
            user_profile.save()
        if request.FILES.get('profile_picture') != None:
            profile_picture  = request.FILES.get('profile_picture')
            first_name  = request.POST['first_name']
            last_name  = request.POST['last_name']
            address  = request.POST['address']
            group = request.POST['group']
            specialty  = request.POST['specialty']
            phone_number  = request.POST['phone_number']

            user_profile.profile_picture  = profile_picture 
            user_profile.first_name  = first_name 
            user_profile.last_name  =  last_name 
            user_profile.address= address
            user_profile.group = group
            user_profile.specialty = specialty
            user_profile.phone_number = phone_number
            user_profile.save()
        
        return redirect('home')
    return render(request, 'settings.html', {'user_profile': user_profile})


#@login_required(login_url='signin')
#def upload(request):
#    if request.method == 'POST':
#        user = request.user.username
#        image = request.FILES.get('image')
#        nature_travail = request.POST['nature_travail']
#        lieu = request.POST['lieu']
#        date_travo = request.POST['date_travo']
#        type_ouvrier = request.POST['type_ovrier']
#        nombre_ouvrier = request.POST['nombre_ouvrier']
#      
#
#        new_post = Post.objects.create(user=user, image=image,nature_travail=nature_travail,lieu=lieu,date_travo=date_travo,typeOuvrier=type_ouvrier,nombre_ouvrier=nombre_ouvrier)
#        new_post.save()
#
#        return redirect('home')
#    else:
#        return render(request, 'addanonce.html')

def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image')
        nature_travail = request.POST['nature_travail']
        lieu = request.POST['lieu']
        date_travo = request.POST['date_travo']
        type_ouvrier = request.POST.get('typeOuvrier')
        nombre_ouvrier = request.POST['nombreOuvrier']

        new_post = Post.objects.create(
            user=user,
            image=image,
            nature_travail=nature_travail,
            lieu=lieu,
            date_travo=date_travo,
            type_ouvrier=type_ouvrier,
            nombre_ouvrier=nombre_ouvrier
        )
        new_post.save()

        return redirect('home')
    else:
        return render(request, 'addanonce.html')





from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, LikePost

@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = get_object_or_404(Post, id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()

    redirect_url = reverse('home')
    return redirect(redirect_url)




@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
    }
    return render(request, 'mesannonces.html', context)

#@login_required(login_url='signin')
#def favoris(request, pk):
    #user_object = User.objects.get(username=pk)
    #user_profile = Profile.objects.get(user=user_object)
    #user_posts = Post.objects.filter(user=pk)
    #user_likes=LikePost.objects.filter(user=pk)
    #user_like_length = len(user_likes)
    #context = {
        #'user_object': user_object,
        #'user_profile': user_profile,
        #'user_posts': user_posts,
        #'user_like_length': user_like_length,
    #}
    #return render(request, 'favoris.html', context)



#@login_required(login_url='signin')
#def search(request):
#    user_object = User.objects.get(username=request.user.username)
#    user_profile = Profile.objects.get(user=user_object)
#
#    if request.method == 'POST':
#        username = request.POST['username']
#        username_object = User.objects.filter(username__icontains=username)
#
#        username_profile = []
#        username_profile_list = []
#
#        for users in username_object:
#            username_profile.append(users.id)
#
#        for ids in username_profile:
#            profile_lists = Profile.objects.filter(id_user=ids)
#            username_profile_list.append(profile_lists)
#        
#        username_profile_list = list(chain(*username_profile_list))
#    return render(request, 'ouvriers.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})


from django.shortcuts import render
from .models import LikePost

from django.shortcuts import render
from .models import LikePost, Post
@login_required(login_url='signin')
def liked_posts(request, username):
    liked_posts = LikePost.objects.filter(username=username).values('post_id')
    post_ids = [liked_post['post_id'] for liked_post in liked_posts]
    posts = Post.objects.filter(id__in=post_ids)
    
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        if post_id:
            LikePost.objects.filter(username=username, post_id=post_id).delete()
            # Vous pouvez également ajouter d'autres actions à effectuer après la suppression du like, si nécessaire
             # Ajouter un message de confirmation
        messages.success(request, "Le like a été supprimé avec succès.")
  # Mise à jour d'autres modèles
        updated_posts = Post.objects.filter(id=post_id)
        for post in updated_posts:
            post.no_of_likes -= 1
            post.save()
    
    context = {
        'liked_posts': posts
    }
    return render(request, 'liked_posts.html', context)
@login_required(login_url='signin')
def delete_like(request, post_id):
    if request.method == 'POST':
        username = request.user.username
        LikePost.objects.filter(username=username, post_id=post_id).delete()
        # Autres actions après la suppression du like
        
    return redirect('liked_posts', username=request.user.username)










from django.shortcuts import render
from .models import LikePost, Post
@login_required(login_url='signin')
def liked_users(request, post_id):
    liked_posts = LikePost.objects.filter(post_id=post_id)  # Récupère tous les objets LikePost du post spécifié
    usernames = [liked_post.username for liked_post in liked_posts]  # Liste des usernames des utilisateurs ayant aimé le post
    
    profiles = Profile.objects.filter(user__username__in=usernames)  # Récupère les profils correspondant aux usernames
    
    return render(request, 'ouvrier.html', {'profiles': profiles})



#LOTO 25 43 ------------------------------------------------------------------------------------------------

@login_required(login_url='signin')
def ouvriers_detail(request, post_id):
    post = Post.objects.get(id=post_id)  # Récupère le poste spécifique en fonction de l'ID

    liked_posts = LikePost.objects.filter(post_id=post.id)  # Récupère tous les objets LikePost liés à ce poste
    usernames = [liked_post.username for liked_post in liked_posts]  # Liste des noms d'utilisateur des utilisateurs ayant aimé le poste

    profiles = Profile.objects.filter(user__username__in=usernames)  # Récupère les profils correspondant aux utilisateurs ayant aimé le poste

    return render(request, 'ouvrierdetail.html', {'post': post, 'profiles': profiles})




# views.py
from django.shortcuts import render, get_object_or_404
from .models import Post
@login_required(login_url='signin')
def modify_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        # Récupérer les données du formulaire
        nature_travail = request.POST.get('nature_travail')
        lieu = request.POST.get('lieu')
        date_travo = request.POST.get('date_travo')
        ouvrier = request.POST.get('ouvrier')

        # Mettre à jour les attributs du post
        post.nature_travail = nature_travail
        post.lieu = lieu
        post.date_travo = date_travo
        post.ouvrier = ouvrier

        # Enregistrer les modifications dans la base de données
        post.save()

        # Rediriger vers la page de détails du post modifié
        return redirect('profile', post_id=post.id)

    return render(request, 'modify_post.html', {'post': post})



from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required





from django.shortcuts import render
from .models import Metier

def liste_metiers(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids[]')
        for metier_id in selected_ids:
            metier = Metier.objects.get(id=int(metier_id))
            valeur = int(request.POST.get(f'valeur_{metier_id}'))
            metier.valeur = valeur
            metier.save()
    metiers = Metier.objects.all()
    return render(request, 'liste_metiers.html', {'metiers': metiers})



from django.shortcuts import render
from .models import Post

from django.db.models import Q

from django.shortcuts import render
from .models import Post

import re
from django.shortcuts import render
from django.db.models import Q
from .models import Post

def remove_accents(text):
    # Remplacer les caractères accentués par leurs équivalents sans accents
    replacements = {
        'i': '[iíìîï]',
        'o': '[oóòôö]',
        'u': '[uúùûü]',
        'c': '[cç]',
    }
    for char, pattern in replacements.items():
        text = re.sub(pattern, char, text, flags=re.IGNORECASE)
    return text

def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query')

        # Filtrer les annonces en fonction de la requête de recherche
        posts = Post.objects.all()

        if search_query:
            # Normaliser les mots de recherche en supprimant les accents
            search_query_normalized = remove_accents(search_query.lower())
            
            # Utiliser des expressions régulières pour la recherche insensible aux accents
            regex_query = f'(?i){search_query_normalized}'
            posts = posts.filter(
                Q(nature_travail__iregex=regex_query) |
                Q(type_ouvrier__iregex=regex_query) |
                Q(lieu__iregex=regex_query)
            )

        context = {
            'posts': posts
        }

        return render(request, 'search.html', context)

    return render(request, 'search.html')

import locale

def formatted_created_at(self):
    # Définir la localisation en français
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    
    # Formater la date et l'heure au format français
    return timezone.localtime(self.created_at).strftime('%d/%m/%Y %H:%M')




def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('home')



# Supposons que cela se trouve dans views.py de ton application Django

from django.shortcuts import render, get_object_or_404
from .models import Profile

def ouvrier_detail(request, username):
    # Récupère le profil correspondant à l'utilisateur avec le nom d'utilisateur spécifié
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, 'ouvrier_detail.html', {'profile': profile})






# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def edit_annonce(request, post_id):
    # Récupérer l'annonce existante à modifier en fonction de l'identifiant (post_id) passé dans l'URL
    annonce = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        # Traiter les données soumises depuis le formulaire de modification
        # Mettre à jour l'annonce existante avec les nouvelles données
        annonce.nature_travail = request.POST['nature_travail']
        annonce.lieu = request.POST['lieu']
        annonce.date_travo = request.POST['date_travo']
        annonce.type_ouvrier = request.POST.get('typeOuvrier')
        annonce.nombre_ouvrier = request.POST['nombreOuvrier']
        annonce.save()

        return redirect('home')
    else:
        # Afficher le formulaire de modification avec les informations préremplies de l'annonce existante
        return render(request, 'edit_annonce.html', {'annonce': annonce})
