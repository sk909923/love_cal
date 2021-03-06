from flask import Flask,request,jsonify,render_template
import psycopg2
from config import config
import json,logging



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
        if request.form:
            # data=request.form.to_dict(flat=False)
            data=request.form
            nameone = data['nameone']
            nametwo = data['nametwo']
            relationship = data['relationship']
            ageone = data['ageone']
            agetwo = data['agetwo']
            res1 = get_val(relationship, nameone)
            res2 = get_val(relationship, nametwo)
            percentage = str(res1) + str(res2)
            final = {"percentage": percentage,"nameone":nameone, "ageone":ageone,"agetwo":agetwo,
                     "nametwo":nametwo,"relationship":relationship}
            return jsonify(final)

        if request.is_json:
            jsonval = request.json
            nameone = jsonval['nameone']
            nametwo = jsonval['nametwo']
            relation = jsonval['relationship']
            res1 = get_val(relation, nameone)
            res2 = get_val(relation, nametwo)
            final_res = str(res1) + str(res2)
            return jsonify(final_res)
    return render_template('Home.html')

@app.route('/postDB',methods=["POST","GET"])
def postDB():
    logging.info('hello')
    if request.method == "POST":
        print("got request method POST")
    if request.is_json:
        print("is json")
        data = request.get_json()
        return jsonify(data)
        # columns = ",".join(data.keys())
        # values = "VALUES({})".format(",".join(["%s" for _ in data.values()]))
        # insert_stmt = "INSERT INTO loveCalculator ({}) {} RETURNING id".format(columns, values)
        #
        # conn = None
        # last_inserted_id = None
        # try:
        #     # read database configuration
        #     params = config()
        #     # connect to the PostgreSQL database
        #     conn = psycopg2.connect(**params)
        #     # create a new cursor
        #     cur = conn.cursor()
        #     # execute the INSERT statement
        #     values = list(map(lambda x: x, data.values()))
        #     cur.execute(insert_stmt, values)
        #     print("value inserted ")
        #     conn.commit()
        #     res = cur.fetchone()
        #     last_inserted_id = res[0]
        #     # print(last_inserted_id)
        #     cur.close()
        # except (Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
        #
        # return jsonify({"last_id": last_inserted_id})

    #     print("type of data {}".format(type(data)))  # type dict
    #     print("data as string {}".format(json.dumps(data)))
    #     print("keys {}".format(json.dumps(data.keys())))
    # return jsonify(message='success')
    # jsonval = request.json
    #
    # print(jsonval)
    #
    # """ insert a new vendor into the vendors table """
    # data = jsonval


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81,debug=True)




