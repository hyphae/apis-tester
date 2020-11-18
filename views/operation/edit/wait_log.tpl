% import config
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
				<li>Message : <input type="text" name="message" value="{{_s(operation.getMessage())}}"></li>
				<li>Timeout : <input type="text" name="timeoutS" value="{{_s(operation.getTimeoutS())}}"> (s)</li>
			</ul>
		</div>
	</form>
	<div>
		<input type="button" class="saveOperationButton" value="Save" onclick="saveOperation('{{operation.getId()}}')" />
		<input type="button" class="deleteOperationButton" value="Delete" onclick="deleteOperation('{{operation.getId()}}')" />
		<input type="button" class="moveOperationButton" value="▲" onclick="moveOperation('{{operation.getId()}}', 'up')" />
		<input type="button" class="moveOperationButton" value="▼" onclick="moveOperation('{{operation.getId()}}', 'down')" />
	</div>
</li>
