% import constant, config
% from util import toString as _s
<li id="{{operation.getId()}}">
	<div>{{operation.getTitle()}}</div>
	<form>
		<input type="hidden" name="id" value="{{operation.getId()}}">
		<input type="hidden" name="type" value="{{operation.getType()}}">
		<div>
			<ul>
				<li>Unit Id : <select type="text" name="unitId" onchange="operation_set_apis_operation_mode_unitId_changed('{{operation.getId()}}', this.value)">
					<option value=""></option>
					% for aUnit in config.units:
						<option value="{{aUnit['id']}}"
							% if aUnit['id'] == operation.getUnitId():
								selected="selected"
							% end
						>{{aUnit['name']}}</option>
					% end
				</select></li>
				<li class="show-unitId- hide-unitId-ANY">Global Operation Mode : <select type="text" name="globalOperationMode">
					<option value=""></option>
					% for aMode in constant.apis_global_operation_modes:
						<option value="{{aMode}}"
							% if aMode == operation.getGlobalOperationMode():
								selected="selected"
							% end
						>{{aMode}}</option>
					% end
				</select></li>
				<li class="hide-unitId- show-unitId-ANY">Local Operation Mode : <select type="text" name="localOperationMode">
					<option value=""></option>
					% for aMode in constant.apis_local_operation_modes:
						<option value="{{aMode}}"
							% if aMode == operation.getLocalOperationMode():
								selected="selected"
							% end
						>{{aMode}}</option>
					% end
				</select></li>
			</ul>
		</div>
	</form>
	<div>
		<input type="button" class="saveOperationButton" value="Save" onclick="saveOperation('{{operation.getId()}}')" />
		<input type="button" class="deleteOperationButton" value="Delete" onclick="deleteOperation('{{operation.getId()}}')" />
		<input type="button" class="moveOperationButton" value="▲" onclick="moveOperation('{{operation.getId()}}', 'up')" />
		<input type="button" class="moveOperationButton" value="▼" onclick="moveOperation('{{operation.getId()}}', 'down')" />
	</div>
	<script>operation_set_apis_operation_mode_unitId_changed('{{operation.getId()}}', '{{_s(operation.getUnitId())}}')</script>
</li>
