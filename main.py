from flask import Flask, request, session, render_template,redirect, url_for
import sql

app = Flask(__name__)
app.secret_key = 'any random string'



@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'OPTIONS', 'PUT', 'PATCH', 'COPY', 'OPTIONS', 'LINK', 'UNLINK', 'PURGE', 'LOCK', 'UNLOCK', 'PROPFIND', 'VIEW'])
def index():



    query="SELECT * FROM statistics WHERE TYPE='{}';".format(request.method)
    methods = sql.query(query)


    if methods is None:

        query = "INSERT INTO statistics (`TYPE`, `VALUE`) VALUES ('{}', 1);".format(request.method)

        sql.query(query)

    else:
        print(methods)
        value = methods[0]['VALUE'] + 1

        query = "UPDATE statistics SET `VALUE`={} WHERE TYPE='{}' ;".format(value, methods[0]['TYPE'])
        sql.query(query)




    #query="INSERT INTO statistics (`TYPE`, `VALUE`) VALUES ("


    return render_template('index.html', methods = methods[0])


@app.route('/', methods=['GET', 'POST'])
def route():

    return render_template('root.html')



@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    query = 'SELECT * FROM statistics;'

    return render_template('statistics.html', table=sql.query(query))






if __name__ == "__main__":
    app.run(debug=True)
