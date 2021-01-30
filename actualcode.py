'''Python
data = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
 
@app.route('/')
def home():
 
    return render_template("index.html", blogs=data)
 
@app.route('/post/<num>')
def get_post(num):
    return render_template("post.html", num=num, blogs=data)
'''    
