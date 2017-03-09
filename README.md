## Hi there.

We're really excited you're using Reddit LinkSaver! LinkSaver uses Python and PRAW to automate download of the many images you've saved on Reddit. If you're interested in customizing it for your own purposes, the code is marked up simply so you can understand it.

## Here's what you have to do.

1.  LinkSaver uses Python to do the heavy lifting. Every Mac has Python installed, but it's usually out of date. Run the Terminal command `python -V` to check what version you have installed. If it's less than 3.4, you'll need to [download it](https://www.python.org/).

2.  You'll need to have PIP installed on your computer to easily install PRAW. Visit [their website](https://pip.pypa.io/en/stable/installing/) and download the file `get-pip.py`. Navigate to your Downloads folder in the Terminal, then use the command `python3 get-pip.py` to install it.

3.  You'll need to have PRAW installed on your computer to connect to Reddit. We use PIP to install it. Run this Terminal command to install it.

    `pip install -U praw`
4.  You'll need to create a new script application authorization in your Reddit account. Follow the instructions at [PRAW's website](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application).

## All done?

Open the file `components.py` and input your account and script authorization information. Be sure to follow the instructions in the comments. It does ask for your login information. If you're worried about privacy and security—a fair concern—you can look through the code in the executable file `LinkSaver.py` to see exactly how this information is used. LinkSaver only uses it to connect to your account to download these images.

## Let's try it out.

Using Reddit LinkSaver is pretty simple. Now that you've filled out product, personal, and payment information, you can just navigate to LinkSaver's directory in the Terminal and run this command.

`python3 LinkSaver.py`

Don't use your computer or web browser while the purchase is occurring.

## Problems? Questions? Changes? Send feedback.

If you've got something you want to see changed, [let us know!](https://andrewrva.typeform.com/to/HL4YOt) <script>(function(){var qs,js,q,s,d=document,gi=d.getElementById,ce=d.createElement,gt=d.getElementsByTagName,id='typef_orm_share',b='https://s3-eu-west-1.amazonaws.com/share.typeform.com/';if(!gi.call(d,id)){js=ce.call(d,'script');js.id=id;js.src=b+'share.js';q=gt.call(d,'script')[0];q.parentNode.insertBefore(js,q)}id=id+'_';if(!gi.call(d,id)){qs=ce.call(d,'link');qs.rel='stylesheet';qs.id=id;qs.href=b+'share-button.css';s=gt.call(d,'head')[0];s.appendChild(qs,s)}})()</script>

Copyright © 2017 All Rights Reserved.
