
my_host = 'localhost'
my_port = 10000

is_emulation = False

emulator_host = '0.0.0.0'
emulator_port = 4390

apis_web_host = '0.0.0.0'
apis_web_budo_emulator_port = 43830
apis_web_api_server_port = 9999

#apis_log_group_address = 'FF02:0:0:0:0:0:0:1'
apis_log_group_address = '224.2.2.4'
apis_log_port = 8888

units = [
	{
		'id' : 'E001',
		'name' : 'E001',
		'host' : '0.0.0.0',
		'dcdc_port' : 4380,
		'emu_port' : 8080,
	},
	{
		'id' : 'E002',
		'name' : 'E002',
		'host' : '0.0.0.0',
		'dcdc_port' : 4380,
		'emu_port' : 8080,
	},
	{
		'id' : 'E003',
		'name' : 'E003',
		'host' : '0.0.0.0',
		'dcdc_port' : 4380,
		'emu_port' : 8080,
	},
	{
		'id' : 'E004',
		'name' : 'E004',
		'host' : '0.0.0.0',
		'dcdc_port' : 4380,
		'emu_port' : 8080,
	},
]

default_control_dcdc_command = 'MODE'
default_control_dcdc_mode = 'WAIT'
default_grid_voltage_v = 350
default_grid_current_a = 2.3
default_droop_ratio = 0

default_deal_grid_current_a = 2
default_deal_amount_wh = 100
default_point_per_wh = 10
default_efficient_grid_voltage_v = 330

default_error_level = 'ERROR'
default_error_extent = 'LOCAL'
default_error_category = 'HARDWARE'

default_wait_log_timeout_s = 30

default_wait_duration_s = 5

default_apis_global_operation_mode = 'Run'
default_apis_local_operation_mode = None
