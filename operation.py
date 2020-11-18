
import logging.config, six, uuid, time, datetime, pytz, urllib, urllib.request, json, socket, re, struct
from threading import Thread
from abc import ABCMeta, abstractmethod
import config, constant
from util import toValue as _v
from util import toString as _s

logger = logging.getLogger(__name__)

####

@six.add_metaclass(ABCMeta)
class Operation(object):
	def __init__(self, type_, title_):
		self.__id_ = str(uuid.uuid4())
		self.__type_ = type_
		self.__title = title_
	def getId(self):
		return self.__id_
	def getType(self):
		return self.__type_
	def getTitle(self):
		return self.__title
		pass
	def _findUnitById(self, val):
		for aUnit in config.units:
			if aUnit['id'] == val:
				return aUnit
		raise RuntimeError('no unit found by id : ' + val)
	@abstractmethod
	def save(self, dic):
		pass
	def dump(self):
		dic = {'type' : self.getType()}
		self._dump(dic)
		return dic
	@abstractmethod
	def _dump(self, dic):
		pass
	def run(self, log, results):
		log.add('[ ' + self.getTitle() + ' ] started')
		try:
			r = self._run(log)
			log.add('[ ' + self.getTitle() + ' ] finished')
			results.append(r)
		except Exception as e:
			log.add('[ ' + self.getTitle() + ' ] failed : ' + str(type(e)) + ' ' + str(e.message))
			results.append(False)
	@abstractmethod
	def _run(self, log):
		pass

class SetApisOperationMode(Operation):
	def __init__(self):
		super(SetApisOperationMode, self).__init__('set_apis_operation_mode', 'Set APIS Operation Mode')
		self.__unitId = None
		self.__globalOperationMode = config.default_apis_global_operation_mode
		self.__localOperationMode = config.default_apis_local_operation_mode
	def save(self, dic):
		self.__unitId = _v(str, dic.get('unitId'))
		self.__globalOperationMode = _v(str, dic.get('globalOperationMode'))
		self.__localOperationMode = _v(str, dic.get('localOperationMode'))
	def _dump(self, dic):
		dic['unitId'] = self.__unitId
		dic['globalOperationMode'] = self.__globalOperationMode
		dic['localOperationMode'] = self.__localOperationMode
	def getUnitId(self):
		return self.__unitId
	def getGlobalOperationMode(self):
		return self.__globalOperationMode
	def getLocalOperationMode(self):
		return self.__localOperationMode
	def _run(self, log):
		value = self.getGlobalOperationMode() if self.getUnitId() is None else self.getLocalOperationMode()
		code = constant.apis_operation_mode_2_code[_s(value)]
		url = 'http://' + config.apis_web_host + ':' + _s(config.apis_web_budo_emulator_port) + '/setOperationMode'
		data = urllib.parse.urlencode({
			'unitId' : _s(self.getUnitId()),
			'value' : code,
		})
		url += '?' + data
		log.add('  url : ' + url)
		res = urllib.request.urlopen(url, timeout = 1).read()
		log.add('  response : ' + res.decode('utf-8').strip())
		log.add('  done')
		return True

class ControlDcdc(Operation):
	def __init__(self):
		super(ControlDcdc, self).__init__('control_dcdc', 'Control DCDC')
		self.__unitId = None
		self.__command = config.default_control_dcdc_command
		self.__mode = config.default_control_dcdc_mode
		self.__gridVoltageV = config.default_grid_voltage_v
		self.__gridCurrentA = config.default_grid_current_a
		self.__droopRatio = config.default_droop_ratio
	def save(self, dic):
		self.__unitId = _v(str, dic.get('unitId'))
		self.__command = _v(str, dic.get('command'))
		self.__mode = _v(str, dic.get('mode'))
		self.__gridVoltageV = _v(float, dic.get('gridVoltageV'))
		self.__gridCurrentA = _v(float, dic.get('gridCurrentA'))
		self.__droopRatio = _v(float, dic.get('droopRatio'))
	def _dump(self, dic):
		dic['unitId'] = self.__unitId
		dic['command'] = self.__command
		dic['mode'] = self.__mode
		dic['gridVoltageV'] = self.__gridVoltageV
		dic['gridCurrentA'] = self.__gridCurrentA
		dic['droopRatio'] = self.__droopRatio
	def getUnitId(self):
		return self.__unitId
	def getCommand(self):
		return self.__command
	def getMode(self):
		return self.__mode
	def getGridVoltageV(self):
		return self.__gridVoltageV
	def getGridCurrentA(self):
		return self.__gridCurrentA
	def getDroopRatio(self):
		return self.__droopRatio
	def _run(self, log):
		unitId = _s(self.getUnitId())
		com = _s(self.getCommand())
		url = None
		if config.is_emulation:
			log.add('  emulator')
			url = 'http://' + config.emulator_host + ':' + _s(config.emulator_port)
			if com == 'MODE':
				code = constant.dcdc_mode_2_code[self.getMode()]
				url += '/set/dcdc/' + unitId + '?mode=' + code + '&dvg=' + _s(self.getGridVoltageV()) + '&dig=' + _s(self.getGridCurrentA()) + '&drg=' + _s(self.getDroopRatio())
			elif com == 'VOLTAGE':
				url += '/set/dcdc/voltage/' + unitId + '?dvg=' + _s(self.getGridVoltageV()) + '&drg=' + _s(self.getDroopRatio())
			elif com == 'CURRENT':
				url += '/set/dcdc/current/' + unitId + '?dig=' + _s(self.getGridCurrentA())
			else:
				raise RuntimeError('bad command : ' + _s(com))
		else:
			log.add('  actual device')
			unit = self._findUnitById(unitId)
			url = 'http://' + unit['host'] + ':' + _s(unit['dcdc_port'])
			if com == 'MODE':
				code = constant.dcdc_mode_2_code[self.getMode()]
				url += '/remote/set?mode=' + code + '&dvg=' + _s(self.getGridVoltageV()) + '&dig=' + _s(self.getGridCurrentA()) + '&drg=' + _s(self.getDroopRatio())
			elif com == 'VOLTAGE':
				url += '/remote/set/voltage?dvg=' + _s(self.getGridVoltageV()) + '&drg=' + _s(self.getDroopRatio())
			elif com == 'CURRENT':
				url += '/remote/set/current?dig=' + _s(self.getGridCurrentA())
			else:
				raise RuntimeError('bad command : ' + _s(com))
		log.add('  url : ' + url)
		res = urllib.request.urlopen(url, timeout = 5).read()
		log.add('  response : ' + res.decode('utf-8').strip())
		log.add('  done')
		return True

class GenerateDeal(Operation):
	def __init__(self):
		super(GenerateDeal, self).__init__('generate_deal', 'Generate Deal')
		self.__dischargeUnitId = None
		self.__chargeUnitId = None
		self.__dealGridCurrentA = config.default_deal_grid_current_a
		self.__dealAmountWh = config.default_deal_amount_wh
		self.__pointPerWh = config.default_point_per_wh
		self.__dischargeUnitEfficientGridVoltageV = config.default_efficient_grid_voltage_v
		self.__chargeUnitEfficientGridVoltageV = config.default_efficient_grid_voltage_v
		self.__testFeature = {'dcdc' : {}}
	def save(self, dic):
		self.__dischargeUnitId = _v(str, dic.get('dischargeUnitId'))
		self.__chargeUnitId = _v(str, dic.get('chargeUnitId'))
		self.__dealGridCurrentA = _v(float, dic.get('dealGridCurrentA'))
		self.__dealAmountWh = _v(float, dic.get('dealAmountWh'))
		self.__pointPerWh = _v(float, dic.get('pointPerWh'))
		self.__dischargeUnitEfficientGridVoltageV = _v(float, dic.get('dischargeUnitEfficientGridVoltageV'))
		self.__chargeUnitEfficientGridVoltageV = _v(float, dic.get('chargeUnitEfficientGridVoltageV'))
		self.__testFeature = {'dcdc' : {}}
		if _v(bool, dic.get('testFeature.dcdc.failBeforeActivate')):
			self.__testFeature['dcdc']['failBeforeActivate'] = True
		if _v(bool, dic.get('testFeature.dcdc.failAfterActivate')):
			self.__testFeature['dcdc']['failAfterActivate'] = True
		if _v(bool, dic.get('testFeature.dcdc.failBeforeAuthorize')):
			self.__testFeature['dcdc']['failBeforeAuthorize'] = True
		if _v(bool, dic.get('testFeature.dcdc.failAfterAuthorize')):
			self.__testFeature['dcdc']['failAfterAuthorize'] = True
		if _v(bool, dic.get('testFeature.dcdc.failBeforeWarmUp')):
			self.__testFeature['dcdc']['failBeforeWarmUp'] = True
		if _v(bool, dic.get('testFeature.dcdc.failAfterWarmUp')):
			self.__testFeature['dcdc']['failAfterWarmUp'] = True
		if _v(bool, dic.get('testFeature.dcdc.failBeforeCompensate')):
			self.__testFeature['dcdc']['failBeforeCompensate'] = True
		if _v(bool, dic.get('testFeature.dcdc.failAfterCompensate')):
			self.__testFeature['dcdc']['failAfterCompensate'] = True
		if _v(bool, dic.get('testFeature.dcdc.failBeforeStop')):
			self.__testFeature['dcdc']['failBeforeStop'] = True
		if _v(bool, dic.get('testFeature.dcdc.failAfterStop')):
			self.__testFeature['dcdc']['failAfterStop'] = True
		if _v(bool, dic.get('testFeature.dcdc.failBeforeDeactivate')):
			self.__testFeature['dcdc']['failBeforeDeactivate'] = True
		if _v(bool, dic.get('testFeature.dcdc.failAfterDeactivate')):
			self.__testFeature['dcdc']['failAfterDeactivate'] = True
	def _dump(self, dic):
		dic['dischargeUnitId'] = self.__dischargeUnitId
		dic['chargeUnitId'] = self.__chargeUnitId
		dic['dealGridCurrentA'] = self.__dealGridCurrentA
		dic['dealAmountWh'] = self.__dealAmountWh
		dic['pointPerWh'] = self.__pointPerWh
		dic['dischargeUnitEfficientGridVoltageV'] = self.__dischargeUnitEfficientGridVoltageV
		dic['chargeUnitEfficientGridVoltageV'] = self.__chargeUnitEfficientGridVoltageV
		for k, v in self.__testFeature['dcdc'].items():
			dic['testFeature.dcdc.' + k] = v
	def getDischargeUnitId(self):
		return self.__dischargeUnitId
	def getChargeUnitId(self):
		return self.__chargeUnitId
	def getDealGridCurrentA(self):
		return self.__dealGridCurrentA
	def getDealAmountWh(self):
		return self.__dealAmountWh
	def getPointPerWh(self):
		return self.__pointPerWh
	def getDischargeUnitEfficientGridVoltageV(self):
		return self.__dischargeUnitEfficientGridVoltageV
	def getChargeUnitEfficientGridVoltageV(self):
		return self.__chargeUnitEfficientGridVoltageV
	def getTestFeature(self):
		return self.__testFeature
	def _run(self, log):
		deal = {}
		deal['createDateTime'] = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y/%m/%d-%H:%M:%S')
		deal['type'] = 'discharge'
		deal['unitId'] = self.getDischargeUnitId()
		deal['requestUnitId'] = self.getDischargeUnitId()
		deal['acceptUnitId'] = self.getChargeUnitId()
		deal['dischargeUnitId'] = self.getDischargeUnitId()
		deal['chargeUnitId'] = self.getChargeUnitId()
		deal['dealGridCurrentA'] = self.getDealGridCurrentA()
		deal['dealAmountWh'] = self.getDealAmountWh()
		deal['pointPerWh'] = self.getPointPerWh()
		if self.getDischargeUnitEfficientGridVoltageV() is not None:
			deal['dischargeUnitEfficientGridVoltageV'] = self.getDischargeUnitEfficientGridVoltageV()
		if self.getChargeUnitEfficientGridVoltageV() is not None:
			deal['chargeUnitEfficientGridVoltageV'] = self.getChargeUnitEfficientGridVoltageV()
		deal['testFeature'] = {}
		if 0 < len(self.__testFeature['dcdc']):
			deal['testFeature']['dcdc'] = self.__testFeature['dcdc']
		val = json.dumps(deal)
		url = 'http://' + config.apis_web_host + ':' + _s(config.apis_web_api_server_port) + '/deal'
		log.add('  url : ' + url)
		log.add('  data : ' + val)
		data = urllib.parse.urlencode({'json' : val})
		res = urllib.request.urlopen(url, data.encode('utf-8'), timeout = 1).read()
		log.add('  response : ' + res.decode('utf-8').strip())
		log.add('  done')
		return True

class GenerateError(Operation):
	def __init__(self):
		super(GenerateError, self).__init__('generate_error', 'Generate Error')
		self.__unitId = None
		self.__category = config.default_error_category
		self.__extent = config.default_error_extent
		self.__level = config.default_error_level
		self.__message = None
	def save(self, dic):
		self.__unitId = _v(str, dic.get('unitId'))
		self.__category = _v(str, dic.get('category'))
		self.__extent = _v(str, dic.get('extent'))
		self.__level = _v(str, dic.get('level'))
		self.__message = _v(str, dic.get('message'))
	def _dump(self, dic):
		dic['unitId'] = self.__unitId
		dic['category'] = self.__category
		dic['extent'] = self.__extent
		dic['level'] = self.__level
		dic['message'] = self.__message
	def getUnitId(self):
		return self.__unitId
	def getCategory(self):
		return self.__category
	def getExtent(self):
		return self.__extent
	def getLevel(self):
		return self.__level
	def getMessage(self):
		return self.__message
	def _run(self, log):
		url = 'http://' + config.apis_web_host + ':' + _s(config.apis_web_api_server_port) + '/error'
		data = urllib.parse.urlencode({
			'unitId' : self.getUnitId(),
			'category' : self.getCategory(),
			'extent' : self.getExtent(),
			'level' : self.getLevel(),
			'message' : self.getMessage(),
		})
		log.add('  url : ' + url)
		log.add('  data : ' + data)
		res = urllib.request.urlopen(url, data.encode('utf-8'), timeout = 1).read()
		log.add('  response : ' + res.decode('utf-8').strip())
		log.add('  done')
		return True

class WaitLog(Operation):
	def __init__(self):
		super(WaitLog, self).__init__('wait_log', 'Wait Log')
		self.__unitId = None
		self.__message = None
		self.__timeoutS = config.default_wait_log_timeout_s
		self.__sock = None
		self.__doWaitLogRunning = False
	def __del__(self):
		if self.__sock:
			self.__sock.close()
	def save(self, dic):
		self.__unitId = _v(str, dic.get('unitId'))
		self.__message = _v(str, dic.get('message'))
		self.__timeoutS = _v(float, dic.get('timeoutS'))
	def _dump(self, dic):
		dic['unitId'] = self.__unitId
		dic['message'] = self.__message
		dic['timeoutS'] = self.__timeoutS
	def getUnitId(self):
		return self.__unitId
	def getMessage(self):
		return self.__message
	def getTimeoutS(self):
		return self.__timeoutS
	def _run(self, log):
		family, socktype, proto, canonname, sockaddr = socket.getaddrinfo(config.apis_log_group_address, config.apis_log_port, socket.AF_UNSPEC, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE)[0]
		log.add('  family    : ' + repr(family))
		log.add('  socktype  : ' + repr(socktype))
		log.add('  proto     : ' + repr(proto))
		log.add('  canonname : ' + repr(canonname))
		log.add('  sockaddr  : ' + repr(sockaddr))
		self.__sock = socket.socket(family, socktype, proto)
		self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
		self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.__sock.settimeout(5)
		if family == socket.AF_INET6:
			self.__sock.bind(sockaddr)
		elif family == socket.AF_INET:
			self.__sock.bind(('0.0.0.0', sockaddr[1]))
			group = socket.inet_pton(family, config.apis_log_group_address)
			mreq = struct.pack('4sL', group, socket.INADDR_ANY)
			self.__sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
		else:
			raise RuntimeError('unknown address family : ' + family)
		log.add('  waiting for log : \'' + _s(self.getMessage()) + '\', from unit : ' + _s(self.getUnitId()))
		results = []
		self.__doWaitLogRunning = True
		t = Thread(target = self.__doWaitLog, args = (results,))
		t.daemon = True
		t.start()
		t.join(self.getTimeoutS())
		self.__doWaitLogRunning = False
		self.__sock.close()
		self.__sock = None
		if 0 < len(results):
			log.add('  log received : ' + results[0])
			log.add('  done')
			return True
		else:
			log.add('  timed out')
			return False
	def __doWaitLog(self, results):
		while self.__doWaitLogRunning:
			try:
				data = self.__sock.recv(8192).decode('utf-8').strip()
				logger.debug('#### waiting log #### ' + data)
				if self.getUnitId() is not None:
					if not data.startswith('[[' + self.getUnitId() + ']] ') and not data.startswith('[[[apis-main:' + self.getUnitId() + ']]] '):
						continue
				if self.getMessage() is not None:
					if not re.search(self.getMessage(), data):
						continue
				results.append(data)
				break
			except Exception as e:
				pass

class Wait(Operation):
	def __init__(self):
		super(Wait, self).__init__('wait', 'Wait')
		self.__durationS = config.default_wait_duration_s
	def save(self, dic):
		self.__durationS = _v(float, dic.get('durationS'))
	def _dump(self, dic):
		dic['durationS'] = self.__durationS
	def getDurationS(self):
		return self.__durationS
	def _run(self, log):
		log.add('  waiting ' + _s(self.getDurationS()) + ' (s)')
		time.sleep(self.getDurationS())
		log.add('  done')
		return True

####

__operations = [
	SetApisOperationMode(),
	ControlDcdc(),
	GenerateDeal(),
	GenerateError(),
	WaitLog(),
	Wait(),
]

def getOperations():
	return __operations

def createByType(val):
	for op in __operations:
		if op.getType() == val:
			clazz = type(op)
			return clazz()
	raise RuntimeError('bad operation type : ' + val)

