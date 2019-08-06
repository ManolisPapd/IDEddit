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


#credit ruda https://stackoverflow.com/a/28015122/2606441
class Tree(object):
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def sub_exists(request):
    exists = True
    try:
        handler.subreddits.search_by_name(request, exact=True)
    except NotFound:
        exists = False
    return exists


def print_comments(parent, branch):
    t = Tree('EMPTY_TREE')
    for child in parent:
        if isinstance(child, MoreComments):
            continue
        try:
            print(child.body + "\t children: " + format(len(child.replies)) + "\n")
            #init node with current comment
            t = Tree(child.body)
        except AttributeError:
            continue
        if len(child.replies) > 0: #to child auto einai pateras giati exei paidia
            for grand in child.replies:
                if isinstance(grand, MoreComments):
                    continue
                try:
                    print(grand.body + "\t children: " + format(len(grand.replies)) + "\n")
                    print_comments(grand.replies, 0)


                except AttributeError:
                    continue
    return t





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


        # nodeList = [Tree('Test1'), Tree('2')]
        # node = Tree('Test', nodeList)
        # print(len(node.children))
        t = print_comments(submission.comments, Tree("IDEddit_FIRST_CALL"))
        print(
            t.name +"\n No. of children: "+
            format(len(t.children)))









