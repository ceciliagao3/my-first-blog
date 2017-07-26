from django.shortcuts import render

def post_list(request):
    published_posts = Post.objects.filter(published_date__lte=timezone.now()
            ).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts'})

# Create your views here.
