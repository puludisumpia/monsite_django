from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import Post, Contact, Subscribe
from .form import ContactForm, SubscribeForm


def postlist(request):
    form = SubscribeForm()
    articles = Post.objects.filter(status=1).order_by("-date")
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/post_list.html", {"posts": posts, "form": form})


def postdetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})


def apropos(request):
    return render(request, "blog/apropos.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            content = form.cleaned_data.get("content")

            # Sauvegarde dans la base de donnée
            ajout_contact = Contact(
                name=name,
                email=email,
                content=content
            )
            ajout_contact.save()

            # Envoi email de confirmation
            subject = "Confirmation reception de votre message"
            body = f"Bonjour {name}, \n" \
                   f"Nous vous confirmons la reception de votre message. \n" \
                   f"Et nous mettons tout en oeuvre pour vous répondre dans les meilleurs délais."
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            messages.success(
                request,
                "Votre message a été envoyé avec succès",
                "success"
            )
            return redirect("contact")
        else:
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})

