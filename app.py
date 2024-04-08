from flask import Flask,request,jsonify, render_template
from model.main import recommendcontent,recommendrating


app=Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html') 

@app.route('/option/<option_name>')
def option(option_name):
    if option_name == 'content':
        return render_template('movie_recommendations.html')
    elif option_name == 'rating':
        return render_template('rating_recommendations.html')
    else:
        return render_template("error.html")


@app.route('/rating', methods = ['POST'])
def rating_based():
    
    genre = request.json['genre']
    lang = request.json['lang']
    rating = request.json['rating']
    num = request.json['num']
    
    if genre and lang and rating and num:
        try:
            rating = float(rating[0])
            num = int(num)
        except ValueError:
            print("in error")
            return jsonify({'success': "false","msg":"invalid request"},400)
        
        result = recommendrating(genre, lang, float(rating),int(num))
        
        return jsonify({"success":"true","data":result,"msg":"data fetched"})
    else:
        return ({"success":"false","msg":"invalid request"},400)
    
    
 
    
@app.route('/content',methods = ['post'])
def content_based():
  
    series_name = request.json['series_name']
    n = request.json['num_recommendations']
    
    if series_name and n:
        try:
            n = int(n)
        except ValueError:
            print("exception occured")
            return jsonify({'success':"false","msg": "Number of recommendations must be numbers!"},400)
        result = recommendcontent(series_name, n)
        
        print("result",result)
        
        return jsonify({"success":"true","data":result,"msg":"request succesfull"})
    else:
        return jsonify({"success":"false","msg":"please make valid entries"},400)
    
    

if __name__ == '__main__':
    app.run(debug=True)