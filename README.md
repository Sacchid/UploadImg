# Upload Images &amp; Display them using Flask &amp; Flask-Dropzone

[Implementation of Medium Article: Upload multiple images with Python, Flask and Flask-Dropzone][1]

In order to handle **.JPG** as well as .jpg, I have declare custom `NIMAGES`as: 

> `NIMAGES = tuple('JPG jpg jpe jpeg png gif svg bmp'.split())
> photos = UploadSet('photos', NIMAGES)`

TO-DO - Pop-up error message

----------
## About - 
While going through following medium article: [Upload multiple images with Python, Flask and Flask-Dropzone][1] , I got `UploadNotAllowed error ` for **.JPG** images. 

**(Uppercase .JPG, no error for lowercase .jpg images)**


GitHub links - [GitHub link of medium article ][2], [GitHub link of my implementation][4]


----------


In order to restrict uploads to images,`UploadSet('photos', IMAGES)` was used

> where, `IMAGES` are defined in `flask_upload.py` as : 

>`IMAGES = tuple('jpg jpe jpeg png gif svg bmp'.split())` 

---

So, In order to handle **.JPG** as well as .jpg, I have declare custom `NIMAGES`as: 

> `NIMAGES = tuple('JPG jpg jpe jpeg png gif svg bmp'.split())
> photos = UploadSet('photos', NIMAGES)`

Which works.


----------

To do - 
 1. While handling `UploadNotAllowed error` in exception, I tried to use  [flask_toastr][3] to display pop-up: Wrong Image Type, but with Status code 302, it was re-directed to homepage without showing pop-up.


  [1]: https://medium.com/@dustindavignon/upload-multiple-images-with-python-flask-and-flask-dropzone-d5b821829b1d "Medium Article"
  [2]: https://raw.githubusercontent.com/ddavignon/flask-multiple-file-upload/master/app.py "Medium/Original github code"
  [3]: https://github.com/wiltonsr/Flask-Toastr "Pop-up using Flask-Toastr"
  [4]: https://github.com/Sacchid/UploadImg "Github link of my implementation"
