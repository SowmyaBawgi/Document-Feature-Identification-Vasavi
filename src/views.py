from flask import redirect,send_from_directory
import os
from .functions import UserActions
from src import app
from .classify import *

@app.route('/')
def start():
    global user
    user=UserActions()
    return user.reset()

@app.route('/home/', methods=['GET', 'POST'])
def main():
    global user
    user=UserActions()
    return user.upload_file()

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    return user.delete_file(filename)


@app.route('/view/<filename>')
def views_file(filename):
    print(os.getcwd())
    path=os.getcwd()+app.config['VIEW']
    print(path)
    return send_from_directory(path,
                               filename)


@app.route('/classify/', methods=['POST'])
def classify():
    uploadedfiles=user.fetch_files()
    classified={}
    dict_words = getwords_dict()
    for file in uploadedfiles:
        filepath=os.path.join(app.config['UPLOAD_FOLDER'], file)
        cfolder=classify_file(filepath, dict_words)
        classified.update({file:cfolder})
    return user.show_output(classified)

@app.route('/getzip/', methods=['POST'])
def getzip():
    return user.download_zip()

@app.route('/display/', methods=['POST'])
def display():
    return user.display_classifiedfiles()




