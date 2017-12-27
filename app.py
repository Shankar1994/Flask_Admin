from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
#admin.add_view(ModelView(User, db.session))
#admin.add_view(ModelView(Post, db.session))

if __name__ == "__main__":
	app.run(debug=True) 
