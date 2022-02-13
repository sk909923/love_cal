from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
def count_fun(flames,argument):
    final_result=[]
    for i in argument:
        result=flames.count(i)
        final_result.append(result)
    return final_result

def get_val(json_obj,name):
    fun=lambda a:a
    flames,argument=list(map(fun,json_obj)),name
    num=count_fun(flames,argument)
    nameone=sum(num)
    return nameone

@app.route('/',methods=["POST","GET"])
def love_logic():
    if request.method =="POST":
        jsonval = request.json
        nameone = jsonval['nameone']
        nametwo = jsonval['nametwo']
        relation = jsonval['relation']
        res1 = get_val(relation, nameone)
        res2 = get_val(relation, nametwo)
        final_res = str(res1) + str(res2)
        return jsonify(final_res)
    return render_template('Home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81,debug=True)




