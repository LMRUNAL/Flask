from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']='static:///posts.db'
db=SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    auther = db.Column(db.String(20),nullable=False,default='N/A')
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return 'BlogPost'+ str(self.id)

all_posts =[{
    'title':'Post 1',
    'content':'This is about  post 1 contents',
    'auther': 'Mrunal'
    },
{ 'title': 'post 2',
  'content' : 'This is about post 2'}]
@app.route("/index")
def index():
    return render_template("i.html")


@app.route('/posts')
def posts():
    return render_template('posts.html',posts=all_posts)

@app.route("/home/<string:name>/posts/<int:id>")
def stud(name,id):
    return "hello,"+ name+ ",5and your id is: "+str(id)


@app.route("/onlyget", methods=["GET"])
def get_req():
    return "you can only get this webpage."
if __name__=="__main__":
    app.run(debug=True)
