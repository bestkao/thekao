from handler import *

"""
In order to be graded correctly for this homework, there are a
few things to keep in mind. We'll be grading your web app by
POSTing to your form and retrieving the text that has been
encoded with ROT13. There are a few main issues you need to keep
in mind in order for this to work:
The textarea form element where the user inputs the text to
encode must be named 'text'. In other words, you must have
'textarea name="text"' for us to post to. The form method must
be POST, not GET. You must enter the full url into the supplied
textbox above, including the path. For example, our example app
is running at http://udacity-cs253.appspot.com/unit2/rot13, but

if we instead only entered http://udacity-cs253.appspot.com/
then the grading script would not work. Don't forget to escape
your output!
"""

class Rot13(Handler):
    def get(self):
        self.render('rot13-form.html')

    def post(self):
        rot13 = ''
        text = self.request.get('text')
        if text:
        	# Python's built-in function to encode w/rot13
            rot13 = text.encode('rot13')

        self.render('rot13-form.html', text = rot13)