from prawcore import NotFound
from mypackage import handler
from praw.models import MoreComments, Submission
from anytree import Node, RenderTree


class Post:
    def __init__(self, id, title, body, url, score, subreddit, number_of_comments):
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


def print_comments(incoming, parent_node):
    results = Node("↑ " + format(incoming.score) + "\n" + incoming.body + " - /u/" + incoming.author.name, parent=parent_node)
    if len(incoming.replies) > 0:
        for child in incoming.replies:
            if isinstance(child, MoreComments):
                continue
            print_comments(child, results)

    return results


class Reddit():
    def call_posts(request, sorting):
        if sub_exists(request):
            posts = []
            subreddit = handler.subreddit(request)
            default_sorting = subreddit.hot(limit=100)
            if sorting is "hot":
                print("HOT REQUEST")
                default_sorting = subreddit.hot(limit=100)
            elif sorting is "new":
                print("NEW REQUEST")
                default_sorting = subreddit.new(limit=100)
            elif sorting is "controversial":
                print("CONTROVERSIAL REQUEST")
                default_sorting = subreddit.controversial(limit=100)
            elif sorting is "rising":
                print("RISING REQUEST")
                default_sorting = subreddit.rising(limit=100)
            for post_from_request in default_sorting:
                posts.append(
                    Post(
                        post_from_request,
                        post_from_request.title,
                        post_from_request.selftext,
                        post_from_request.url,
                        post_from_request.score,
                        "/" + str(post_from_request.subreddit),
                        post_from_request.num_comments
                    )
                )
            return posts
        else:
            return []

    def load_comments(id):
        submission = Submission(handler, id)
        submission.comment_sort = 'top'
        parent = submission.comments
        parent_node = Node("Comments")
        for child in parent:
            if isinstance(child, MoreComments):
                continue
            try:
                print_comments(child, parent_node)
            except AttributeError:
                continue
        # for pre, fill, node in RenderTree(parent_node):
        #     print("%s%s" % (pre, node.name))
        return parent_node

