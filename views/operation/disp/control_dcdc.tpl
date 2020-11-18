% from util import toString as _s
<li id="{{operation.getId()}}">
	<div>{{operation.getTitle()}}</div>
	<div>
		<ul>
			<li>Unit Id : {{_s(operation.getUnitId())}}</li>
			<li>Command : {{_s(operation.getCommand())}}</li>
			<li class="hide-command- show-command-MODE hide-command-VOLTAGE hide-command-CURRENT">Mode : {{_s(operation.getMode())}}</li>
			<li class="hide-command- show-command-MODE show-command-VOLTAGE hide-command-CURRENT">Grid Voltage : {{_s(operation.getGridVoltageV())}} (V)</li>
			<li class="hide-command- show-command-MODE hide-command-VOLTAGE show-command-CURRENT">Grid Current : {{_s(operation.getGridCurrentA())}} (A)</li>
			<li class="hide-command- show-command-MODE show-command-VOLTAGE hide-command-CURRENT">Droop Ratio : {{_s(operation.getDroopRatio())}}</li>
		</ul>
	</div>
	<div>
		<input type="button" class="editOperationButton" value="Edit" onclick="editOperation('{{operation.getId()}}')" />
		<input type="button" class="deleteOperationButton" value="Delete" onclick="deleteOperation('{{operation.getId()}}')" />
		<input type="button" class="moveOperationButton" value="▲" onclick="moveOperation('{{operation.getId()}}', 'up')" />
		<input type="button" class="moveOperationButton" value="▼" onclick="moveOperation('{{operation.getId()}}', 'down')" />
	</div>
	<script>operation_control_dcdc_command_changed('{{operation.getId()}}', '{{_s(operation.getCommand())}}')</script>
</li>
