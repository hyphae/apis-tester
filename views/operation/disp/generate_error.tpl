% from util import toString as _s
<li id="{{operation.getId()}}">
	<div>{{operation.getTitle()}}</div>
	<div>
		<ul>
			<li>Unit Id : {{_s(operation.getUnitId())}}</li>
			<li>Category : {{_s(operation.getCategory())}}</li>
			<li>Extent : {{_s(operation.getExtent())}}</li>
			<li>Level : {{_s(operation.getLevel())}}</li>
			<li>Message : {{_s(operation.getMessage())}}</li>
		</ul>
	</div>
	<div>
		<input type="button" class="editOperationButton" value="Edit" onclick="editOperation('{{operation.getId()}}')" />
		<input type="button" class="deleteOperationButton" value="Delete" onclick="deleteOperation('{{operation.getId()}}')" />
		<input type="button" class="moveOperationButton" value="▲" onclick="moveOperation('{{operation.getId()}}', 'up')" />
		<input type="button" class="moveOperationButton" value="▼" onclick="moveOperation('{{operation.getId()}}', 'down')" />
	</div>
</li>
