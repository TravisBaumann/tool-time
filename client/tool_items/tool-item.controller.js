import { merge } from 'ramda';

function ToolItemController() {
	const ctrl = this;
	ctrl.showControls = false;
	ctrl.editMode = false;
	ctrl.toolToEdit = {};

	ctrl.setShowControls = function setShowControls(showControls) {
		ctrl.showControls = showControls;
	};

	ctrl.setEditMode = function setEditMode(editMode) {
		ctrl.editMode = editMode;
		ctrl.toolToEdit = merge({}, ctrl.tool);
	};

	ctrl.editTool = function editTool(toolToEdit) {
		ctrl.update({ toolToUpdate: toolToEdit });
		ctrl.tool = toolToEdit;
		ctrl.editMode = false;
	};

	ctrl.deleteTool = function deleteTool() {
		ctrl.delete({ toolToDelete: ctrl.tool });
	};

	ctrl.checkTool = function checkTool() {		
		ctrl.tool.checked = !ctrl.tool.checked;
		ctrl.update({ toolToUpdate: ctrl.tool });
	};
}

export default ToolItemController;