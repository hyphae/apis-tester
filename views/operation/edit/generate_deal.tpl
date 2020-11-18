% import config
% from util import toString as _s
<li id="{{operation.getId()}}">
	<div>{{operation.getTitle()}}</div>
	<form>
		<input type="hidden" name="id" value="{{operation.getId()}}">
		<input type="hidden" name="type" value="{{operation.getType()}}">
		<div>
			<ul>
				<li>Discharge Unit Id : <select type="text" name="dischargeUnitId">
					<option value=""></option>
					% for aUnit in config.units:
						<option value="{{aUnit['id']}}"
							% if aUnit['id'] == operation.getDischargeUnitId():
								selected="selected"
							% end
						>{{aUnit['name']}}</option>
					% end
				</select></li>
				<li>Charge Unit Id : <select type="text" name="chargeUnitId">
					<option value=""></option>
					% for aUnit in config.units:
						<option value="{{aUnit['id']}}"
							% if aUnit['id'] == operation.getChargeUnitId():
								selected="selected"
							% end
						>{{aUnit['name']}}</option>
					% end
				</select></li>
				<li>Deal Grid Current : <input type="text" name="dealGridCurrentA" value="{{_s(operation.getDealGridCurrentA())}}"> (A)</li>
				<li>Deal Amount : <input type="text" name="dealAmountWh" value="{{_s(operation.getDealAmountWh())}}"> (Wh)</li>
				<li>Point Per Wh : <input type="text" name="pointPerWh" value="{{_s(operation.getPointPerWh())}}"></li>
				<li>Discharge Unit Efficient Grid Voltage : <input type="text" name="dischargeUnitEfficientGridVoltageV" value="{{_s(operation.getDischargeUnitEfficientGridVoltageV())}}"> (V)</li>
				<li>Charge Unit Efficient Grid Voltage : <input type="text" name="chargeUnitEfficientGridVoltageV" value="{{_s(operation.getChargeUnitEfficientGridVoltageV())}}"> (V)</li>
				<li>Test Feature : <input type="checkbox" name="testFeature" value="True" onchange="operation_generate_deal_testFeature_changed('{{operation.getId()}}', this.checked)"
					%if 0 < len(operation.getTestFeature().get("dcdc")):
						checked="checked"
					%end
				>
					<ul class="hide-testFeature-False show-testFeature-True">
						<li>Dcdc : <input type="checkbox" name="testFeature-dcdc" value="True" onchange="operation_generate_deal_testFeature_dcdc_changed('{{operation.getId()}}', this.checked)"
							%if 0 < len(operation.getTestFeature().get("dcdc")):
								checked="checked"
							%end
						>
							<ul class="hide-testFeature-dcdc-False show-testFeature-dcdc-True">
								<li>Fail Before Activate : <input type="checkbox" name="testFeature.dcdc.failBeforeActivate"
									% if operation.getTestFeature().get('dcdc').get('failBeforeActivate'):
										checked="checked"
									% end
								></li>
								<li>Fail After Activate : <input type="checkbox" name="testFeature.dcdc.failAfterActivate"
									% if operation.getTestFeature().get('dcdc').get('failAfterActivate'):
										checked="checked"
									% end
								></li>
								<li>Fail Before Authorize : <input type="checkbox" name="testFeature.dcdc.failBeforeAuthorize"
									% if operation.getTestFeature().get('dcdc').get('failBeforeAuthorize'):
										checked="checked"
									% end
								></li>
								<li>Fail After Authorize : <input type="checkbox" name="testFeature.dcdc.failAfterAuthorize"
									% if operation.getTestFeature().get('dcdc').get('failAfterAuthorize'):
										checked="checked"
									% end
								></li>
								<li>Fail Before Warm Up : <input type="checkbox" name="testFeature.dcdc.failBeforeWarmUp"
									% if operation.getTestFeature().get('dcdc').get('failBeforeWarmUp'):
										checked="checked"
									% end
								></li>
								<li>Fail After Warm Up : <input type="checkbox" name="testFeature.dcdc.failAfterWarmUp"
									% if operation.getTestFeature().get('dcdc').get('failAfterWarmUp'):
										checked="checked"
									% end
								></li>
								<li>Fail Before Compensate : <input type="checkbox" name="testFeature.dcdc.failBeforeCompensate"
									% if operation.getTestFeature().get('dcdc').get('failBeforeCompensate'):
										checked="checked"
									% end
								></li>
								<li>Fail After Compensate : <input type="checkbox" name="testFeature.dcdc.failAfterCompensate"
									% if operation.getTestFeature().get('dcdc').get('failAfterCompensate'):
										checked="checked"
									% end
								></li>
								<li>Fail Before Stop : <input type="checkbox" name="testFeature.dcdc.failBeforeStop"
									% if operation.getTestFeature().get('dcdc').get('failBeforeStop'):
										checked="checked"
									% end
								></li>
								<li>Fail After Stop : <input type="checkbox" name="testFeature.dcdc.failAfterStop"
									% if operation.getTestFeature().get('dcdc').get('failAfterStop'):
										checked="checked"
									% end
								></li>
								<li>Fail Before Deactivate : <input type="checkbox" name="testFeature.dcdc.failBeforeDeactivate"
									% if operation.getTestFeature().get('dcdc').get('failBeforeDeactivate'):
										checked="checked"
									% end
								></li>
								<li>Fail After Deactivate : <input type="checkbox" name="testFeature.dcdc.failAfterDeactivate"
									% if operation.getTestFeature().get('dcdc').get('failAfterDeactivate'):
										checked="checked"
									% end
								></li>
							</ul>
						</li>
					</ul>
				</li>
			</ul>
		</div>
	</form>
	<div>
		<input type="button" class="saveOperationButton" value="Save" onclick="saveOperation('{{operation.getId()}}')" />
		<input type="button" class="deleteOperationButton" value="Delete" onclick="deleteOperation('{{operation.getId()}}')" />
		<input type="button" class="moveOperationButton" value="▲" onclick="moveOperation('{{operation.getId()}}', 'up')" />
		<input type="button" class="moveOperationButton" value="▼" onclick="moveOperation('{{operation.getId()}}', 'down')" />
	</div>
	<script>operation_generate_deal_testFeature_changed('{{operation.getId()}}', '{{_s(0 < len(operation.getTestFeature().get("dcdc")))}}')</script>
	<script>operation_generate_deal_testFeature_dcdc_changed('{{operation.getId()}}', '{{_s(0 < len(operation.getTestFeature().get("dcdc")))}}')</script>
</li>
