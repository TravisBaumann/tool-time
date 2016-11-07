
function toolAPIService($resource) {
	const api = {
		tools: $resource('/api/tool_items/:id',
			{ id: '@id' },
			{
				update: {
					method: 'PUT',
				},
			}),
	};

	return api;
}

export default toolAPIService;