% from util import toString as _s
<li id="{{operation.getId()}}">
	<div>{{operation.getTitle()}}</div>
	<div>
		<ul>
			<li>Discharge Unit Id : {{_s(operation.getDischargeUnitId())}}</li>
			<li>Charge Unit Id : {{_s(operation.getChargeUnitId())}}</li>
			<li>Deal Grid Current : {{_s(operation.getDealGridCurrentA())}} (A)</li>
			<li>Deal Amount : {{_s(operation.getDealAmountWh())}} (Wh)</li>
			<li>Point Per Wh : {{_s(operation.getPointPerWh())}}</li>
			<li>Discharge Unit Efficient Grid Voltage : {{_s(operation.getDischargeUnitEfficientGridVoltageV())}} (V)</li>
			<li>Charge Unit Efficient Grid Voltage : {{_s(operation.getChargeUnitEfficientGridVoltageV())}} (V)</li>
			<li>Test Feature :
				<ul class="hide-testFeature-False show-testFeature-True">
					<li>Dcdc :
						<ul class="hide-testFeature-dcdc-False show-testFeature-dcdc-True">
							<li>Fail Before Activate : {{_s(True if operation.getTestFeature().get('dcdc').get('failBeforeActivate') else None)}}</li>
							<li>Fail After Activate : {{_s(True if operation.getTestFeature().get('dcdc').get('failAfterActivate') else None)}}</li>
							<li>Fail Before Authorize : {{_s(True if operation.getTestFeature().get('dcdc').get('failBeforeAuthorize') else None)}}</li>
							<li>Fail After Authorize : {{_s(True if operation.getTestFeature().get('dcdc').get('failAfterAuthorize') else None)}}</li>
							<li>Fail Before Warm Up : {{_s(True if operation.getTestFeature().get('dcdc').get('failBeforeWarmUp') else None)}}</li>
							<li>Fail After Warm Up : {{_s(True if operation.getTestFeature().get('dcdc').get('failAfterWarmUp') else None)}}</li>
							<li>Fail Before Compensate : {{_s(True if operation.getTestFeature().get('dcdc').get('failBeforeCompensate') else None)}}</li>
							<li>Fail After Compensate : {{_s(True if operation.getTestFeature().get('dcdc').get('failAfterCompensate') else None)}}</li>
							<li>Fail Before Stop : {{_s(True if operation.getTestFeature().get('dcdc').get('failBeforeStop') else None)}}</li>
							<li>Fail After Stop : {{_s(True if operation.getTestFeature().get('dcdc').get('failAfterStop') else None)}}</li>
							<li>Fail Before Deactivate : {{_s(True if operation.getTestFeature().get('dcdc').get('failBeforeDeactivate') else None)}}</li>
							<li>Fail After Deactivate : {{_s(True if operation.getTestFeature().get('dcdc').get('failAfterDeactivate') else None)}}</li>
						</ul>
					</li>
				</ul>
			</li>
		</ul>
	</div>
	<div>
		<input type="button" class="editOperationButton" value="Edit" onclick="editOperation('{{operation.getId()}}')" />
		<input type="button" class="deleteOperationButton" value="Delete" onclick="deleteOperation('{{operation.getId()}}')" />
		<input type="button" class="moveOperationButton" value="▲" onclick="moveOperation('{{operation.getId()}}', 'up')" />
		<input type="button" class="moveOperationButton" value="▼" onclick="moveOperation('{{operation.getId()}}', 'down')" />
	</div>
	<script>operation_generate_deal_testFeature_changed('{{operation.getId()}}', '{{_s(0 < len(operation.getTestFeature().get("dcdc")))}}')</script>
	<script>operation_generate_deal_testFeature_dcdc_changed('{{operation.getId()}}', '{{_s(0 < len(operation.getTestFeature().get("dcdc")))}}')</script>
</li>
