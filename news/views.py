from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Article, Comment
from .forms import ArticleForm, CommentForm

articles_count = 2

def index(request):
    articles = Article.objects.all()

    paginator = Paginator(articles, articles_count)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    previous_page = ''
    next_page = ''

    if page.has_previous():
        previous_page = page.previous_page_number

    if page.has_next():
        next_page = page.next_page_number

    context = {
        "page": page,
        "previous_page": previous_page,
        "next_page": next_page,
        "is_paginated": is_paginated,
        "news_object": True}

    return render(request, 'news/index.html', context=context)


class ArticleDetail(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug__iexact=slug)
        try:
            image_url = article.image.url
        except:
            image_url = "."

        return render(request, 'news/article_detail.html', context={"article": article, "admin_object": article, "image_url": image_url, "news_object": True})


class ArticleCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = ArticleForm()
        return render(request, 'news/article_create_form.html', context={"form": form, "news_object": True})

    def post(self, request):
        bound_form = ArticleForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_article = bound_form.save()
            return redirect(new_article)
        return render(request, 'news/article_create_form.html', context={"form": bound_form, "news_object": True})
    raise_exception = True


class ArticleDelete(LoginRequiredMixin, View):
    def get(self, request, slug):
        article = Article.objects.get(slug__iexact=slug)
        return render(request, 'news/article_delete_form.html', context={"article": article, "news_object": True})

    def post(self, request, slug):
        article = Article.objects.get(slug__iexact=slug)
        article.delete()
        return redirect(reverse('articles_list_url'))
    raise_exception = True


class ArticleUpdate(LoginRequiredMixin, View):
    def get(self, request, slug):
        article = Article.objects.get(slug__iexact=slug)
        bound_form = ArticleForm(instance=article)
        return render(request, 'news/article_update_form.html', context={"form": bound_form, "article": article, "news_object": True})
    def post(self, request, slug):
        article = Article.objects.get(slug__iexact=slug)
        bound_form = ArticleForm(request.POST, request.FILES, instance=article)

        if bound_form.is_valid():
            new_article = bound_form.save()
            return redirect(new_article)
        return render(request, 'news/article_update_form', context={"form": bound_form, "article": article, "news_object": True})
    raise_exception = True


# comments


class ArticleCommentCreate(LoginRequiredMixin, View):
    def get(self, request, slug):
        form = CommentForm()
        article = Article.objects.get(slug__iexact=slug)
        return render(request, 'news/article_comment_create_form.html', context={"form": form, "article": article, "news_object": True})

    def post(self, request, slug):
        bound_form = CommentForm(request.POST)
        if bound_form.is_valid():
            new_comment = bound_form.save()
            return redirect(Article.objects.get(slug__iexact=slug))
        return render(request, 'news/article_comment_create_form.html', context={"form": bound_form, "news_object": True})
    raise_exception = True


class ArticleCommentUpdate(LoginRequiredMixin, View):
    def get(self, request, slug, comment_slug):
        comment = Comment.objects.get(slug__iexact=comment_slug)
        bound_form = CommentForm(instance=comment)
        return render(request, 'news/article_comment_update_form.html', context={"form": bound_form, "comment": comment, "news_object": True})

    def post(self, request, slug, comment_slug):
        comment = Comment.objects.get(slug__iexact=comment_slug)
        article = Article.objects.get(slug__iexact=slug)
        bound_form = CommentForm(request.POST, instance=comment)

        if bound_form.is_valid():
            new_comment = bound_form.save()
            return redirect(article)
        return render(request, 'news/article_comment_update_form.html', context={"form": bound_form, "comment": comment, "news_object": True})
    raise_exception = True


class ArticleCommentDelete(LoginRequiredMixin, View):
    def get(self, request, slug, comment_slug):
        comment = Comment.objects.get(slug__iexact=comment_slug)
        article = Article.objects.get(slug__iexact=slug)
        return render(request, 'news/article_comment_delete_form.html', context={"comment": comment, "article": article, "news_object": True})

    def post(self, request, slug, comment_slug):
        print('delete')
        comment = Comment.objects.get(slug__iexact=comment_slug)
        comment.delete()
        return redirect(Article.objects.get(slug__iexact=slug))
    raise_exception = True
