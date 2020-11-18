#!/usr/bin/env python

import sys, logging.config, json
from bottle import route, post, error, run, template, static_file, request, response
import constant, config, operation, program

logger = logging.getLogger(__name__)

####

@error(404)
def error404(error):
	return "404 not found."

@route('/static/<filename>')
def static(filename):
	return static_file(filename, root='./static')

@route('/')
def index():
	return template(
		'main',
	)

####

@route('/getProgramSequence')
def getProgramSequence():
	try:
		html = ''
		for op in program.getSequence():
			html += template(
				'operation/disp/' + op.getType(),
				operation = op,
			)
		return json.dumps({'html' : html})
	except Exception as e:
		return __exceptionResponse(e)

@route('/addOperation')
def addOperation():
	try:
		type_ = request.params['type']
		op = operation.createByType(type_)
		program.addOperation(op)
		html = template(
			'operation/edit/' + op.getType(),
			operation = op,
		)
		return json.dumps({'html' : html})
	except Exception as e:
		return __exceptionResponse(e)

@route('/saveOperation')
def saveOperation():
	try:
		id_ = request.params['id']
		op = program.operationById(id_)
		op.save(request.params)
		html = template(
			'operation/disp/' + op.getType(),
			operation = op,
		)
		return json.dumps({'html' : html})
	except Exception as e:
		return __exceptionResponse(e)

@route('/editOperation')
def editOperation():
	try:
		id_ = request.params['id']
		op = program.operationById(id_)
		html = template(
			'operation/edit/' + op.getType(),
			operation = op,
		)
		return json.dumps({'html' : html})
	except Exception as e:
		return __exceptionResponse(e)

@route('/moveOperation')
def moveOperation():
	try:
		id_ = request.params['id']
		upDown = request.params['upDown']
		res = program.moveOperationById(id_, upDown)
		return json.dumps({'result' : res})
	except Exception as e:
		return __exceptionResponse(e)

@route('/deleteOperation')
def deleteOperation():
	try:
		id_ = request.params['id']
		op = program.removeOperationById(id_)
		del op
		html = ''
		return json.dumps({'html' : html})
	except Exception as e:
		return __exceptionResponse(e)

####

@route('/startProgram')
def startProgram():
	try:
		res = program.start()
		return json.dumps({'result' : res})
	except Exception as e:
		return __exceptionResponse(e)

@route('/stopProgram')
def stopProgram():
	try:
		res = program.stop()
		return json.dumps({'result' : res})
	except Exception as e:
		return __exceptionResponse(e)

@route('/isProgramRunning')
def isProgramRunning():
	try:
		res = program.isRunning()
		return json.dumps({'result' : res})
	except Exception as e:
		return __exceptionResponse(e)

@route('/getProgramLog')
def getProgramLog():
	try:
		res = program.getLog()
		return json.dumps({'result' : res})
	except Exception as e:
		return __exceptionResponse(e)
@route('/eraseProgramLog')
def eraseProgramLog():
	try:
		res = program.eraseLog()
		return json.dumps({'result' : res})
	except Exception as e:
		return __exceptionResponse(e)

####

@route('/dumpProgram')
def dumpProgram():
	try:
		dic = program.dump()
		return json.dumps({'result' : dic})
	except Exception as e:
		return str(type(e)) + ' ' + e.message

@post('/restoreProgram')
def restoreProgram():
	try:
		info = request.files.get('file')
		if info.filename.endswith('.json'):
			raw = info.file.read()
			data = json.loads(raw)
			program.restore(data)
		else:
			raise RuntimeError('file suffix should be : .json')
	except Exception as e:
		return __exceptionResponse(e)
	return getProgramSequence()

####

def __exceptionResponse(e):
	return json.dumps({'error' : str(type(e)) + ' ' + e.message})

####

def __startWebServer():
	run(server="tornado", host=config.my_host, port=config.my_port, quiet=False, reloader=False)

def main(argv):
	logger.debug('starting tester ...')
	__startWebServer()

####

if __name__ == "__main__":
	logging.config.fileConfig("conf/logger.conf", disable_existing_loggers=False)
	main(sys.argv[1:])
