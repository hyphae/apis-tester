
$(function() {
	$.ajaxSetup({
		cache : false,
	});
	updateSequence();
	updateLog();
	var forceUpdateLog = false;
	$('#addOperationButton').click(function() {
		var val = $('#addOperationTypeSelection').val();
		if (val) {
			$.getJSON('./addOperation', {'type' : val}, function(json) {
				if (json) {
					if (json.error) {
						alert('error : ' + json.error);
					} else {
						$('#addOperationTypeSelection').val('');
						$('#sequence').append(json.html);
						updateDisabled();
					}
				}
			});
		}
	});
	$('#startProgramButton').click(function() {
		$.getJSON('./startProgram', function(json) {
			if (json) {
				if (json.error) {
					alert('error : ' + json.error);
				} else {
					updateDisabled();
					forceUpdateLog = true;
				}
			}
		});
	});
	$('#stopProgramButton').click(function() {
		$.getJSON('./stopProgram', function(json) {
			if (json) {
				if (json.error) {
					alert('error : ' + json.error);
				} else {
					updateDisabled();
				}
			}
		});
	});
	$('#dumpProgramButton').click(function() {
		$.getJSON('./dumpProgram', function(json) {
			if (json) {
				if (json.error) {
					alert('error : ' + json.error);
				} else {
					var data = json.result;
					var elm = document.createElement('a');
					elm.href = window.URL.createObjectURL(new Blob([JSON.stringify(data, null, '\t')], {type : 'application/json'}));
//					elm.target = '_blank';
					{
						var now = new Date();
						var y = now.getFullYear();
						var m = ('0' + (now.getMonth() + 1)).slice(-2);
						var d = ('0' + now.getDate()).slice(-2);
						var hh = ('0' + now.getHours()).slice(-2);
						var mm = ('0' + now.getMinutes()).slice(-2);
						var ss = ('0' + now.getSeconds()).slice(-2);
						elm.download = 'tester-program-' + y + m + d + hh + mm + ss + '.json';
					}
					elm.click();
				}
			}
		});
	});
	$('#restoreProgramButton').click(function() {
		var elm = document.createElement('input');
		elm.type = 'file';
		elm.name = 'file';
		elm.onchange = function() {
			var file = elm.files[0];
			var data = new FormData();
			data.append('file', file);
			$.ajax('/restoreProgram', {
				method : 'POST',
				contentType : false,
				data : data,
				processData : false,
				dataType : 'json',
				success : function(json) {
					if (json.error) {
						alert('error : ' + json.error);
					} else {
						$('#sequence').html(json.html);
					}
				},
			});
			return false;
		};
		elm.click();
	});
	$('#eraseLogButton').click(function() {
		$.getJSON('./eraseProgramLog', function(json) {
			if (json) {
				if (json.error) {
					alert('error : ' + json.error);
				} else {
					forceUpdateLog = true;
				}
			}
		});
	});

	function updateSequence() {
		$.getJSON('./getProgramSequence', function(json) {
			if (json) {
				if (json.error) {
					alert('error : ' + json.error);
				} else {
					$('#sequence').html(json.html);
				}
			}
		});
	}
	function updateLog() {
		$.getJSON('./getProgramLog', function(json) {
			if (json) {
				if (json.error) {
					alert('error : ' + json.error);
				} else {
					$('#log').text(json.result);
					forceUpdateLog = false;
				}
			}
		});
	}
	function updateDisabled() {
		if (0 < $('.saveOperationButton').length) {
			$('#startProgramButton').prop('disabled', true);
			$('#dumpProgramButton').prop('disabled', true);
			$('#restoreProgramButton').prop('disabled', true);
		} else {
			$.getJSON('./isProgramRunning', function(json) {
				if (json) {
					if (json.result) {
						$('input,select').prop('disabled', true);
						$('#stopProgramButton').prop('disabled', false);
					} else {
						$('input,select').prop('disabled', false);
						$('#stopProgramButton').prop('disabled', true);
					}
				}
			});
		}
	}

	setInterval(function() {
		if (forceUpdateLog || !$('#stopProgramButton').prop('disabled')) {
			updateLog();
		}
		updateDisabled();
	}, 1000);
});


function editOperation(opId) {
	$.getJSON('./editOperation', {'id' : opId}, function(json) {
		if (json) {
			if (json.error) {
				alert('error : ' + json.error);
			} else {
				$('#' + opId).replaceWith(json.html);
			}
		}
	});
}
function saveOperation(opId) {
	var query = $('#' + opId).find('form').serialize();
	$.getJSON('./saveOperation', query, function(json) {
		if (json) {
			if (json.error) {
				alert('error : ' + json.error);
			} else {
				$('#' + opId).replaceWith(json.html);
			}
		}
	});
}
function moveOperation(opId, upDown = 'up') {
	$.getJSON('./moveOperation', {'id' : opId, 'upDown' : upDown}, function(json) {
		if (json) {
			if (json.error) {
				alert('error : ' + json.error);
			} else {
				if (json.result) {
					if (upDown == 'up') {
						$('#' + opId).prev().before($('#' + opId));
					} else {
						$('#' + opId).next().after($('#' + opId));
					}
				}
			}
		}
	});
}
function deleteOperation(opId) {
	$.getJSON('./deleteOperation', {'id' : opId}, function(json) {
		if (json) {
			if (json.error) {
				alert('error : ' + json.error);
			} else {
				$('#' + opId).replaceWith(json.html);
			}
		}
	});
}

////

function operation_control_dcdc_command_changed(opId, val) {
	$('#' + opId + ' .hide-command-' + val).hide();
	$('#' + opId + ' .show-command-' + val).show();
}

function operation_generate_deal_testFeature_changed(opId, val) {
	$('#' + opId + ' .hide-testFeature-' + val).hide();
	$('#' + opId + ' .show-testFeature-' + val).show();
}
function operation_generate_deal_testFeature_dcdc_changed(opId, val) {
	$('#' + opId + ' .hide-testFeature-dcdc-' + val).hide();
	$('#' + opId + ' .show-testFeature-dcdc-' + val).show();
}

function operation_set_apis_operation_mode_unitId_changed(opId, val) {
	if (val) val = 'ANY';
	$('#' + opId + ' .hide-unitId-' + val).hide();
	$('#' + opId + ' .show-unitId-' + val).show();
}
