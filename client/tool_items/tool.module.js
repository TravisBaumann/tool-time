import angular from 'angular';
import 'angular-resource';
import 'angular-animate';
import 'angular-filter';

import FlashesModule from '../flashes/flashes.module';

import toolPageComponent from './tool-page.component';
import toolItemComponent from './tool-item.component';
import toolEditComponent from './tool-edit.component';

import toolAPIService from './tool-api.service';

const ToolModule = angular.module('tools', [
	'ngResource',
	'ngAnimate',
	'angular.filter',
	FlashesModule.name,
])
	.config(($resourceProvider) => {
		$resourceProvider.defaults.stripTrailingSlashes = false;
	})
	.config(function($httpProvider) {
       $httpProvider.defaults.xsrfCookieName = 'csrftoken';
       $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
   })
	.factory('toolAPIService', toolAPIService)
	.component('toolPage', toolPageComponent)
	.component('toolItem', toolItemComponent)
	.component('toolEdit', toolEditComponent);

export default ToolModule;