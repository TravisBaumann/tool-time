import { findIndex } from 'ramda';

function ToolPageController(toolAPIService, flashesService, $interval) {
	const ctrl = this;
	ctrl.editedTool = {};


	function getTools() {
		toolAPIService.tools.get().$promise.then((data) => {
			ctrl.tools = data.results;
		});
	};



	getTools();
	$interval(getTools, 50000);

	ctrl.saveTool = function saveTool(editedTool) {
		toolAPIService.tools.save(editedTool).$promise.then((savedTool) => {
			alert (savedTool)
			ctrl.tools = [
				savedTool,
					ctrl.tool,
			];
			ctrl.editedTool = {};
			flashesService.displayMessage('Your post has been uploaded!', 'success');
		});
	};

	ctrl.updateTool = function updateTool(toolToUpdate) {
		toolAPIService.tools.update(toolToUpdate).$promise.then(() => {
			flashesService.displayMessage('Tool Updated', 'success');
		});
	};

	ctrl.deleteTool = function deleteTool(toolToDelete) {
		const findTool = findIndex(item => toolToDelete.id ===item.id);
		const index = findTool(ctrl.tools);

		if (index !== -1) {
			ctrl.tools.splice(index, 1);
		}

		toolAPIService.tools.delete(toolToDelete).$promise.then(() => {
			flashesService.displayMessage('Item Deleted', 'success');
		});
	};

}

export default ToolPageController;