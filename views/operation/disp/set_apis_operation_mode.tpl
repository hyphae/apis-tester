% from util import toString as _s
<li id="{{operation.getId()}}">
	<div>{{operation.getTitle()}}</div>
	<div>
		<ul>
			<li>Unit Id : {{_s(operation.getUnitId())}}</li>
			<li class="show-unitId- hide-unitId-ANY">Global Operation Mode : {{_s(operation.getGlobalOperationMode())}}</li>
			<li class="hide-unitId- show-unitId-ANY">Local Operation Mode : {{_s(operation.getLocalOperationMode())}}</li>
		</ul>
	</div>
	<div>
		<input type="button" class="editOperationButton" value="Edit" onclick="editOperation('{{operation.getId()}}')" />
		<input type="button" class="deleteOperationButton" value="Delete" onclick="deleteOperation('{{operation.getId()}}')" />
		<input type="button" class="moveOperationButton" value="▲" onclick="moveOperation('{{operation.getId()}}', 'up')" />
		<input type="button" class="moveOperationButton" value="▼" onclick="moveOperation('{{operation.getId()}}', 'down')" />
	</div>
	<script>operation_set_apis_operation_mode_unitId_changed('{{operation.getId()}}', '{{_s(operation.getUnitId())}}')</script>
</li>
