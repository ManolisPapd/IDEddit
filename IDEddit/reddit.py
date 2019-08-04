from mypackage import handler


class Post:
    id = 0
    title = ""
    body = ""


class Reddit():
    def call_posts(request):
        subreddit = handler.subreddit('python')
        hot_python = subreddit.hot(limit=5)
        for post_from_request in hot_python:
            print(post_from_request)
        posts = [request,"apple", "banana", "cherry"]
        return posts

