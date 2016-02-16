import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory


# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'doc'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded files
    uploaded_files = request.files.getlist("file[]")
    filenames = []
    for file in uploaded_files:
        # Check if the file is one of the allowed types/extensions
        if file and allowed_file(file.filename):
          
            filename = (file.filename)
            # Move the file form the temporal folder to the upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Save the filename into a list, we'll use it later
            filenames.append(filename)
           
    return render_template('upload.html', filenames=filenames)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



@app.route('/remove', methods=['POST'])
def remove(filename):
    filenames=[]

    if(os.path.isfile(filename)):
        os.remove(app.config['UPLOAD_FOLDER'],filename)

    path = "/uploads"
    dirs = os.listdir(path)

# This would print all the files and directories
    for file in dirs:
        print(file)
        filenames.append(filename)

    return render_template("uploads.html",filenames=filenames)


if __name__ == '__main__':
    app.run(debug=True)
