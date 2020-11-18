
import logging.config, datetime, pytz, time
from threading import Thread
import operation

logger = logging.getLogger(__name__)

####

class Log(object):
	def __init__(self):
		self.__logs = []
	def add(self, val):
		self.__logs.append((datetime.datetime.now(pytz.timezone('Asia/Tokyo')), val,))
	def getAll(self):
		return self.__logs
	def getFormatted(self):
		res = ''
		for (dt, val) in self.__logs:
			res += dt.isoformat() + ' ' + val + '\n'
		return res

class Runner(Thread):
	def __init__(self, sequence):
		super(Runner, self).__init__()
		self.__started = None
		self.__stopping = None
		self.__stopped = None
		self.__aborted = None
		self.__finished = None
		self.__log = Log()
		self.__sequence = sequence
	def run(self):
		self.__ensureNotStarted()
		self.__started = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
		self.__log.add('program started')
		for op in self.__sequence:
			if self.__stopping is not None:
				self.__stop()
				return
			results = []
			t = Thread(target = op.run, args = (self.__log, results,))
			t.daemon = True
			t.start()
			t.join()
			if len(results) == 0 or not results[0]:
				self.__abort()
				return
		self.__finish()
	def stop(self):
		self.__ensureRunning()
		self.__stopping = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
		self.__log.add('stop requested')
	def __stop(self):
		self.__ensureRunning()
		self.__stopped = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
		self.__log.add('program stopped')
	def __abort(self):
		self.__ensureRunning()
		self.__aborted = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
		self.__log.add('program aborted')
	def __finish(self):
		self.__ensureRunning()
		self.__finished = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
		self.__log.add('program finished')
	def isRunning(self):
		return self.__started is not None and self.__stopped is None and self.__aborted is None and self.__finished is None
	def getLog(self):
		return self.__log.getFormatted()
	def eraseLog(self):
		self.__log = Log()
		return True
	def __ensureNotStarted(self):
		if self.__started is not None:
			raise RuntimeError('Runner already started at ' + self.__started.isoformat())
	def __ensureRunning(self):
		if self.__started is None:
			raise RuntimeError('Runner not started')
		elif self.__stopped is not None:
			raise RuntimeError('Runner already stopped at ' + self.__stopped.isoformat())
		elif self.__aborted is not None:
			raise RuntimeError('Runner already aborted at ' + self.__aborted.isoformat())
		elif self.__finished is not None:
			raise RuntimeError('Runner already finished at ' + self.__finished.isoformat())

####

__runner = None

def start():
	if not isRunning():
		time.sleep(1)
		global __runner
		__runner = Runner(__sequence)
	__runner.start()
	return True
def isRunning():
	return __runner is not None and __runner.isRunning()
def stop():
	__runner.stop()
	return True
def getLog():
	if __runner is not None:
		return __runner.getLog()
	else:
		return ''
def eraseLog():
	if __runner is not None:
		return __runner.eraseLog()
	else:
		return True

####

__sequence = []

def getSequence():
	return __sequence

def addOperation(val):
	__sequence.append(val);

def operationById(val):
	for op in __sequence:
		if op.getId() == val:
			return op
	raise RuntimeError('no operation found by id : ' + val)

def moveOperationById(val, upDown):
	op = operationById(val)
	idx = __sequence.index(op)
	if upDown == 'up':
		if 0 < idx:
			__sequence.remove(op)
			__sequence.insert(idx - 1, op)
			return True
		else:
			return False
	elif upDown == 'down':
		if idx < len(__sequence) - 1:
			__sequence.remove(op)
			__sequence.insert(idx + 1, op)
			return True
		else:
			return False
	raise RuntimeError('unknown upDown value : ' + upDown)

def removeOperationById(val):
	op = operationById(val)
	__sequence.remove(op)
	return op

####

def dump():
	seq = []
	for op in __sequence:
		seq.append(op.dump())
	return {'sequence' : seq}

def restore(data):
	result = []
	for aData in data.get('sequence'):
		type_ = aData.get('type')
		op = operation.createByType(type_)
		op.save(aData)
		result.append(op)
	global __sequence
	__sequence = result
