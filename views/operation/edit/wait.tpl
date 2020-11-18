% from util import toString as _s
<li id="{{operation.getId()}}">
	<div>{{operation.getTitle()}}</div>
	<form>
		<input type="hidden" name="id" value="{{operation.getId()}}">
		<input type="hidden" name="type" value="{{operation.getType()}}">
		<div>
			<ul>
				<li>Duration : <input type="text" name="durationS" value="{{_s(operation.getDurationS())}}"> (s)</li>
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
