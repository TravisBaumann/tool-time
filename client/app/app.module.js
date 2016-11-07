import angular from 'angular';

import ToolModule from '../tool_items/tool.module';
import FlashesModule from '../flashes/flashes.module';

import appComponent from './app.component';

const AppModule = angular.module('app', [
	ToolModule.name,
	FlashesModule.name,
])
    .component('app', appComponent);

export default AppModule;
