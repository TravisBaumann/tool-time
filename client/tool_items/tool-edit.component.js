import template from './tool-edit.html';

import ToolEditController from './tool-edit.controller';

const toolEditComponent = {
	template,
	bindings: {
		tool: '<',
		save: '&',
		cancel: '&',
	},
	controller: ToolEditController,
	controllerAs: 'toolEditCtrl',
};

export default toolEditComponent;