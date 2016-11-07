import { merge } from 'ramda';


function ToolEditController() {
	const ctrl = this;
	ctrl.editedTool = {};

	ctrl.$onChanges = function $onChanges() {
		ctrl.editedTool = merge({}, ctrl.tool);
	};

	ctrl.saveTool = function saveTool() {
		ctrl.save({ editedTool: ctrl.editedTool });
	};

	
}

export default ToolEditController;