% import constant, config
% from util import toString as _s
<li id="{{operation.getId()}}">
	<div>{{operation.getTitle()}}</div>
	<form>
		<input type="hidden" name="id" value="{{operation.getId()}}">
		<input type="hidden" name="type" value="{{operation.getType()}}">
		<div>
			<ul>
				<li>Unit Id : <select type="text" name="unitId">
					<option value=""></option>
					% for aUnit in config.units:
						<option value="{{aUnit['id']}}"
							% if aUnit['id'] == operation.getUnitId():
								selected="selected"
							% end
						>{{aUnit['name']}}</option>
					% end
				</select></li>
				<li>Command : <select type="text" name="command" onchange="operation_control_dcdc_command_changed('{{operation.getId()}}', this.value)">
					<option value=""></option>
					% for aCommand in constant.dcdc_control_commands:
						<option value="{{aCommand}}"
							% if aCommand == operation.getCommand():
								selected="selected"
							% end
						>{{aCommand}}</option>
					% end
				</select></li>
				<li class="hide-command- show-command-MODE hide-command-VOLTAGE hide-command-CURRENT">Mode : <select type="text" name="mode">
					<option value=""></option>
					% for aMode in constant.dcdc_modes:
						<option value="{{aMode}}"
							% if aMode == operation.getMode():
								selected="selected"
							% end
						>{{aMode}}</option>
					% end
				</select></li>
				<li class="hide-command- show-command-MODE show-command-VOLTAGE hide-command-CURRENT">Grid Voltage : <input type="text" name="gridVoltageV" value="{{_s(operation.getGridVoltageV())}}"> (V)</li>
				<li class="hide-command- show-command-MODE hide-command-VOLTAGE show-command-CURRENT">Grid Current : <input type="text" name="gridCurrentA" value="{{_s(operation.getGridCurrentA())}}"> (A)</li>
				<li class="hide-command- show-command-MODE show-command-VOLTAGE hide-command-CURRENT">Droop Ratio : <input type="text" name="droopRatio" value="{{_s(operation.getDroopRatio())}}"></li>
			</ul>
		</div>
	</form>
	<div>
		<input type="button" class="saveOperationButton" value="Save" onclick="saveOperation('{{operation.getId()}}')" />
		<input type="button" class="deleteOperationButton" value="Delete" onclick="deleteOperation('{{operation.getId()}}')" />
		<input type="button" class="moveOperationButton" value="▲" onclick="moveOperation('{{operation.getId()}}', 'up')" />
		<input type="button" class="moveOperationButton" value="▼" onclick="moveOperation('{{operation.getId()}}', 'down')" />
	</div>
	<script>operation_control_dcdc_command_changed('{{operation.getId()}}', '{{_s(operation.getCommand())}}')</script>
</li>
