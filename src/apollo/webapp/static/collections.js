// Backbone.js Collections
MessageCollection = PaginatedCollection.extend({
    model: Message,
    baseUrl: '/api/v1/message/',
});

LocationCollection = PaginatedCollection.extend({
	model: Location,
	baseUrl: '/api/v1/location/',
});

IncidentCollection = PaginatedCollection.extend({
	model: Incident,
	baseUrl: '/api/v1/incidents/',
});

ChecklistCollection = PaginatedCollection.extend({
	model: Checklist,
	baseUrl: '/api/v1/checklists/',
});