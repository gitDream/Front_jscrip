import json
import os , sys
import time
import re
import uuid
import threading
#os.chdir('/www/server/panel/')
#sys.path.append( "class/")
#import public
#os.chdir('/messager_demo/app')

from flask import Flask,current_app,session,render_template,send_file,request,redirect,g,url_for,make_response,render_template_string,abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NOqWF5R8sAhPO2paiAc3tJ0adCAqfVoJsw7PH8yLEXUGGLOXWWm3JUgnoII5xsNc'

method_all = ['GET','POST']
@app.route('/',methods=method_all)
def indexl():
    return render_template('demo.html')




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
