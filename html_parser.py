# The attrs tag in the handle_starttag has all the attributes of the html tags. And for getting the attributes we
# to itterate through the attrs.
from html.parser import HTMLParser


class MyHTMLparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("The start tags present in the HTML code are :", tag)
        for i in attrs:
            print("The attributes present in the HTML code are :", i)

    def handle_endtag(self, tag):
        print("The endtags present in the HTML code are :", tag)

    def handle_data(self, data):
        print("The data present in the HTML code are :", data)
       
    def handle_comment(self, data):
        print("The comment present in the HTML code are :", data)


parser = MyHTMLparser()
parser.feed('<html><head><title>Test</title></head >'
            '<body><h1>Parse me!</h1></body></html>')
# In this way you need to feed the raw HTML data into the parser.feed() command.
