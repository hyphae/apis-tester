% import operation
<html lang="ja">
	<head>
		<meta charset="utf-8">
		<title>Tester</title>
		<script src="//code.jquery.com/jquery-3.3.1.min.js"></script>
		<script src="./static/_.js"></script>
		<link rel="stylesheet" href="./static/_.css">
	</head>
	<body>
		<div style="float:left">
			<div>Sequence</div>
			<div>
				<div>
					<ol id="sequence"></ol>
				</div>
				<div>
					<select id="addOperationTypeSelection">
						<option value=""></option>
						% for anOperation in operation.getOperations():
							<option value="{{anOperation.getType()}}">{{anOperation.getTitle()}}</option>
						% end
					</select>
					<input type="button" id="addOperationButton" value="Add" />
				</div>
			</div>
			<div>
				<input type="button" id="startProgramButton" value="Start" disabled="disabled" />
				<input type="button" id="stopProgramButton" value="Stop" disabled="disabled" />
				<input type="button" id="dumpProgramButton" value="Dump" disabled="disabled" />
				<input type="button" id="restoreProgramButton" value="Restore" disabled="disabled" />
			</div>
		</div>
		<div style="float:right">
			<div>Log</div>
			<div><pre id="log"></pre></div>
			<div>
				<input type="button" id="eraseLogButton" value="Erase" disabled="disabled" />
			</div>
		</div>
	</body>
</html>