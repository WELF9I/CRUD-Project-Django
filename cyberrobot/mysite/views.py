from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Etudiant, Article
from .forms import ArticleForm

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    context = {'etudiants': etudiants}
    return render(request, 'etudiants.html', context)



def ajouter_etudiant(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        cin = request.POST['cin']
        tel = request.POST['tel']
        email = request.POST['email']
        Etudiant.objects.create(
            nom=nom,
            prenom=prenom,
            cin=cin,
            tel=tel,
            email=email
        )
        return redirect('liste_etudiants')

    return render(request, 'ajouter_etudiant.html')

def modifier_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)

    if request.method == 'POST':
        etudiant.nom = request.POST['nom']
        etudiant.prenom = request.POST['prenom']
        etudiant.cin = request.POST['cin']
        etudiant.tel = request.POST['tel']
        etudiant.email = request.POST['email']
        etudiant.save()
        return redirect('liste_etudiants')
    return render(request, 'modifier_etudiant.html', {'etudiant': etudiant})

def supprimer_etudiant(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    etudiant.delete()
    return redirect('liste_etudiants')



def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'ajouter_article.html', {'form': form})

def modifier_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'modifier_article.html', {'form': form, 'article': article})

def supprimer_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect('liste_articles')

def home(request):
    return render(request, 'home.html')