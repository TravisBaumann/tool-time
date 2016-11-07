import template from './tool-item.html';

import ToolItemController from './tool-item.controller';

const toolItemComponent = {
	template,
	bindings: {
		tool: '<',
		delete: '&',
		update: '&',
	},
	controller: ToolItemController,
	controllerAs: 'toolItemCtrl',
};

export default toolItemComponent;