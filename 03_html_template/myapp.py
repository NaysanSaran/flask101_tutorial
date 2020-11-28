from flask import Flask, render_template
import os
import random

app = Flask(__name__)


def random_jaden_quote():
    """
    return a random quote from Jaden Smith
    """
    quotes = [
        "Instagram is not the answer.",
        "You can discover everything you need to know about everything by looking at your hands",
        "Being born was the most influential thing that’s ever happened to me, for myself.",
        "When Life Gives You Big Problems, Just Be Happy You Forgot All Your Little Problems.",
        "I'll never read every single book or go to every single place. But I'll die in the trying of it.",
        "The only way to change something is to shock it.",
        "If a cupcake falls from a tree how far away will it be from down.",
        "What is the definition of 'light'?",
        "People Use To Ask Me What Do You Wanna Be When You Get Older And I Would Say What A Stupid Question The Real Question Is What Am I Right Now.",
        "The Lack Of Emotion In My Face Doesn't Mean I'm Unhappy.",
        "I want to be the most durable person on the planet",
        "When The First Animal Went Extinct That Should've Been A Sign.",
        "How Can Mirrors Be Real If Our Eyes Aren't Real.",
        "I'm Glad That Our Distance Makes Us Witness Ourselves From A Different Entrance"
    ]
    quote = "%s -- Jaden Smith" % random.choice(quotes)
    return quote


def random_image():
    """
    Return a random image from the ones in the static/ directory
    """
    img_dir = "./static"
    img_list = os.listdir(img_dir)
    return random.choice(img_list)


@app.route('/')
def myapp():
    quote = random_jaden_quote()
    image = random_image()
    return render_template('index.html', random_quote=quote, random_image=image)



