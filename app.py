from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class, UploadNotAllowed
from werkzeug.utils import secure_filename

from flask_toastr import Toastr
from flask import flash

import os

app = Flask(__name__)
dropzone = Dropzone(app)

app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

toastr = Toastr(app)

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

# USE NIMAGES instead of IMAGES to accept .JPG as IMAGES doesn't accept .JPG images
NIMAGES = tuple('JPG jpg jpe jpeg png gif svg bmp'.split())
photos = UploadSet('photos', NIMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route('/', methods=['GET', 'POST'])
def index():
    # flash("All OK", 'success')
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropszone
    if request.method == 'POST':
        try:
            file_obj = request.files
            for f in file_obj:
                file = request.files.get(f)
                print(file.filename)
                # save the file with to our photos folder
                filename = photos.save(
                    file,
                    name=file.filename
                )

                # append image urls
                file_urls.append(photos.url(filename))

            session['file_urls'] = file_urls
            return "uploading..."
        except UploadNotAllowed as e:
            print(e)
            print("Error handled")
            flash("Unsupported Image type, use another image", 'error')
            # flash("Not So OK: %s" % e, 'error')
        # except Exception as e:
        #     print(e)
        #     # flash("Not So OK: %s" %e, 'error')

    # return dropzone template on GET request
    return render_template('index.html')


@app.route('/results')
def results():
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))

    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)

    return render_template('results.html', file_urls=file_urls)
