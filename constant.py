
error_categories = ['USER', 'HARDWARE', 'LOGIC', 'FRAMEWORK']
error_extents = ['LOCAL', 'GLOBAL']
error_levels = ['WARN', 'ERROR', 'FATAL']

dcdc_control_commands = ['MODE', 'VOLTAGE', 'CURRENT']
dcdc_modes = ['WAIT', 'VOLTAGE_REFERENCE', 'DISCHARGE', 'CHARGE']
dcdc_mode_2_code = {
	'WAIT' : '0x0000',
	'VOLTAGE_REFERENCE' : '0x0014',
	'DISCHARGE' : '0x0002',
	'CHARGE' : '0x0041',
}

apis_global_operation_modes = [
	'Run', 'Soft Stop', 'Force Stop', 'Manual'
]
apis_local_operation_modes = [
	'Soft Stop', 'Force Stop'
]
apis_operation_mode_2_code = {
	'' : '',
	'Run' : 'autonomous',
	'Soft Stop' : 'heteronomous',
	'Force Stop' : 'stop',
	'Manual' : 'manual'
}
