from prawcore import NotFound
from mypackage import handler
from praw.models import MoreComments

class Post:
    def __init__(self, id, title, body, url, score, subreddit,number_of_comments):
        self.id = id
        self.title = title
        self.body = body
        self.url = url
        self.score = score
        self.subreddit = subreddit
        self.number_of_comments = number_of_comments


def sub_exists(request):
    exists = True
    try:
        handler.subreddits.search_by_name(request, exact=True)
    except NotFound:
        exists = False
    return exists


class Reddit():
    def call_posts(request):
        if sub_exists(request):
            posts = []
            subreddit = handler.subreddit(request)
            hot_python = subreddit.hot(limit=20)
            for post_from_request in hot_python:
                posts.append(
                    Post(
                        post_from_request,
                        post_from_request.title,
                        post_from_request.selftext,
                        post_from_request.url,
                        post_from_request.score,
                        "/"+str(post_from_request.subreddit),
                        post_from_request.num_comments
                    )
                )
            return posts
        else:
            return []

    def load_comments(id):
        submission = handler.submission(id)

        #TODO automate it for n replies
        '''
        def print_comments:
            for child in parent:
                print child
                loop(len(child.replies)):
                    recursive: print_comments(child.replies))
        '''
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            print("Comment: " + top_level_comment.body + "\n"+top_level_comment.author.name + "\n")
            #parse comment replies
            print("Replies: " + format(len(top_level_comment.replies)))
            for replyComment in top_level_comment.replies:
                if isinstance(replyComment, MoreComments):
                    continue
                print("\t\t Reply: " + replyComment.body + "\n"+replyComment.author.name)
                print("###Replies of replies: " + format(len(replyComment.replies)))





