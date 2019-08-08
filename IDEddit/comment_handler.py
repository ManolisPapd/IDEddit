class Comment_Handler():
    def list_item_format(counter, score, title, url, subreddit, number):
        list_item = (format(counter) + " | " +
                     format(score) + "\t" +
                     title + "\t" + subreddit + "\n\n\t" + format(number) + " comments" + "\n\n\t" +
                     url + "\n\n")
        return list_item

