from flask import Flask, render_template, request
import pymysql
import datetime

app = Flask(__name__)
data = []
count = 77
call = 77


@app.route('/')
def base():
    return render_template('base/login.html')


@app.route('/personalFile/personalHealth')
def personalHealth():
    global data
    return render_template('personFile/personHealth.html', user=data)


@app.route('/callCenter/callCenter')
def callCenter():
    return render_template('callCenter/callpage.html')


@app.route('/callCenter/callCenter1', methods=['GET', 'POST'])
def callCenter1():
    if request.method == 'POST':
        global count, call, data
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='authMySQLhh@770425zxd',
                             database='zhkydb')
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = str(dt)
        sql = "INSERT INTO sys_call VALUES ('%d', '%s',  %d,  '%s',  %d)" % \
              (call, dt, 1, 'waiting', data[0])
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        db.close()
        call += 1
        return render_template('callCenter/callCenter1.html')
    return render_template('callCenter/callpage.html')


@app.route('/callCenter/callCenter2', methods=['GET', 'POST'])
def callCenter2():
    if request.method == 'POST':
        global count, call, data
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = str(dt)
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='authMySQLhh@770425zxd',
                             database='zhkydb')
        sql = "INSERT INTO sys_call VALUES ('%d', '%s',  %d,  '%s',  %d)" % \
               (call, dt, 2, 'waiting', data[0])
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        db.close()
        call += 1
        return render_template('callCenter/callCenter2.html')
    return render_template('callCenter/callpage.html')


@app.route('/teleconsultation/teleconsultation')
def teleconsultation():
    return render_template('teleconsultation/teleconsultation.html')


@app.route('/EpidemicKnowledgeBase/knowledge')
def knowledge():
    return render_template('EpidemicKnowledgeBase/knowledge.html')


@app.route('/BigDataAnalysis/yiqingAnalysis')
def fenxi():
    return render_template('BigDataAnalysis/BigDataAnalysis.html')


@app.route('/BigDataAnalysis/yiqingmap')
def _map():
    return render_template('BigDataAnalysis/yiqingmap.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('errorPage/404.html'), 404


@app.errorhandler(500)
def page_not_found():
    return render_template('errorPage/404.html'), 500


@app.route('/old/login/input', methods=['GET', 'POST'])
def logi():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        name = request.form.get('name')  # 传入表单对应输入字段的 name 值
        pwd = request.form.get('pwd')
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='authMySQLhh@770425zxd',
                             database='zhkydb')
        sql = str("SELECT * FROM user_old WHERE user_old_logname=" + name + " and user_old_logpasswd=" + pwd + ";")
        cursor = db.cursor()
        cursor.execute(sql)
        global data
        data = list(cursor.fetchone())
        db.close()
        if data is None:
            return render_template('base/input.html')
        else:
            return render_template('base/base.html')
    return render_template('base/input.html')


@app.route('/old/login/zc', methods=['GET', 'POST'])
def call_():
    if request.method == 'POST':
        name = request.form.get('name')
        realname = request.form.get('realname')
        pwd = request.form.get('pwd')
        age = request.form.get('age')
        ID = request.form.get('IDcard')
        address = request.form.get('address')
        telephone = request.form.get('telephone')
        global count
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='authMySQLhh@770425zxd',
                             database='zhkydb')
        sql = "insert into user_old(user_old_id,user_old_name,user_old_age,user_old_IDcard," \
              "user_old_address,user_old_number," \
              "user_old_logname,user_old_logpasswd,user_old_health_document_id)values" \
              "(%d, %s, %d, %s, %s, %s, %s, %s, 0)" % \
              (count, realname, int(age), ID, address, telephone, name, pwd)
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
            db.close()
            count += 1
            global data
            data = [count, name, age, ID, address, telephone]
            return render_template('base/base.html')
        except:
            # 发生错误时回滚
            db.rollback()
            db.close()
            return render_template('base/zc.html')
    return render_template('base/zc.html')


@app.route('/old/login')
def zc():
    return render_template('base/login.html')


@app.route('/old/login/base')
def ma():
    return render_template('base/base.html')


if __name__ == '__main__':
    app.run(debug=True)
