class CommentHandler:
    def list_item_format(counter, score, title, url, subreddit, number):
        list_item = (format(counter) + " | " +
                     format(score) + "\t" +
                     title + "\t" + subreddit + "\n\n\t" + format(number) + " comments" + "\n\n\t" +
                     url + "\n\n")
        return list_item

    def get_stylesheet(self):
        return """
                                                QTreeWidget::item {
                                                  padding: 20px 0;
                                                  border-bottom: 1px solid black;
                                                  max-width: 75ch;

                                                }
                                                QTreeWidget::item:hover {
                                                  background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);
                                                  border: 1px solid #bfcde4;
                                                }
                                                QTreeWidget::item:selected  {
                                                    color: black;
                                                  border-left: 6px solid blue;
                                                  background: #6dadd1;
                                                }

                                                QListWidget::item  {
                                                    background-color: red;
                                                }
                                                QLayout::SetNoConstraint

                                                """

