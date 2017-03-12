## Hi there.

We're really excited you're using KeepIt! KeepIt uses Python and PRAW to automate download of the many images you've saved on Reddit. It can download images from lots of sources, even if they're not directly hosted. This includes Imgur and Flickr "image links" (which aren't really direct image links at all, but HTML files with the image displayed inside them). If you're interested in customizing KeepIt for your own purposes, the code is marked up simply so you can understand it.

## Here's what you have to do.

1.  KeepIt uses Python to do the heavy lifting. Every Mac has Python installed, but it's usually out of date. Run the Terminal command `python -V` to check what version you have installed. If it's less than 3.4, you'll need to [download it](https://www.python.org/).

2.  You'll need to have PIP installed on your computer to easily install PRAW. Visit [their website](https://pip.pypa.io/en/stable/installing/) and download the file `get-pip.py`. Navigate to your Downloads folder in the Terminal, then use the command `python3 get-pip.py` to install it.

3.  You'll need to have PRAW installed on your computer to connect to Reddit. We use PIP to install it. Run this Terminal command to install it.

    `pip install -U praw`
4.  You'll need to create a new script application authorization in your Reddit account. Follow the instructions at [PRAW's website](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application).

## All done?

Open the file `components.py` and input your account and script authorization information. Be sure to follow the instructions in the comments. It does ask for your login information. If you're worried about privacy and security—a fair concern—you can look through the code in the executable file `KeepIt.py` to see exactly how this information is used. KeepIt only uses it to connect to your account to download these images.

## Let's try it out.

Using Reddit KeepIt is pretty simple. Now that you've filled out product, personal, and payment information, you can just navigate to KeepIt's directory in the Terminal and run this command.

`python3 KeepIt.py`

Don't use your computer or web browser while the purchase is occurring.

## Problems? Questions? Changes? Send feedback.

If you've got something you want to see changed, [let us know!](https://andrewrva.typeform.com/to/HL4YOt)
