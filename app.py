# app.py
from flask import Flask
from flask import render_template
from flask import Response

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/coreos-ipxe/<userid>/<sshkeyname>/<instanceid>')
@app.route('/coreos-ipxe/<userid>/<sshkeyname>/<instanceid>/<channel>')
def coreos_ipxe(userid, instanceid, sshkeyname, channel='stable') :
	return render_template(
		'coreos-ipxe',
		userid=userid,
		sshkeyname=sshkeyname,
		sshkey=key(userid, sshkeyname),
		instanceid=instanceid,
		channel=channel
	)

@app.route('/key/<userid>')
@app.route('/key/<userid>/<sshkeyname>')
def key(userid, sshkeyname='id_rsa.pub') :
	return open('keys/{0}/{1}'.format(userid, sshkeyname)).read()

@app.route('/coreos-cloudconfig-template/<userid>/<instanceid>')
def instancetemplate(userid, instanceid) :
	return 'coreos-cloudconfig'

@app.route('/coreos-cloudconfig/<userid>/<sshkeyname>/<instanceid>')
def coreos_cloudconfig(userid, sshkeyname, instanceid) :
	return Response(
		render_template(
			instancetemplate(userid, instanceid),
			key=key(userid, sshkeyname)
		),
		mimetype='text/x-yaml'
		)

@app.route("/ping")
def ping():
	return 'PONG'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
