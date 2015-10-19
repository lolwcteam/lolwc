Riot.QATool.MasteryApp = (function () {
	var dd, fn,
		templates = {
			listPiece: [
				'<div class="listpiece" data-rg-name="{{ modelName }}" data-rg-id="{{ id }}">',
					'{{ img }}',
					'<div class="name">{{ name }}</div>',
				'</div>'
			],
			tooltipPiece: [
				'{{ img }}',
				'<div class="info{{ maxClass }}">',
					'<div class="name">{{ name }}</div>',
					'<div class="rank">Rank: {{ rank }}/{{ max }}</div>',
					'<div class="description">{{ description }}</div>',
				'</div>'
			]
		};
	
	return {
		init: function () {
			dd = Riot.DDragon;
			fn = dd.fn;
			
			dd.addDisplay({
				type: 'mastery_tooltip',
				// Expects: Individual Mastery Object
				success: function(data) {
					var mastery = Riot.QATool.MasteryApp.summoner.findMastery(data.id);
					
					return mastery.getTip();
				}
			});

			dd.addDisplay({
				type: 'mastery_modal',
				// Expects: Individual Item Object
				success: function(data) {
					return fn.format(templates.tooltipPiece, {
						img: this.model.getImg(data.id),
						name: data.name,
						description: data.description
					});
				},
				onReactive: function () {
					return false;
				}
			});
			
			// These list out the individual pieces
			dd.addDisplay({
				type: 'masterypiece',
				// Expects: Individual Item Object
				success: function(data) {
					return fn.format(templates.listPiece, {
						modelName: this.model.name,
						id: data.id,
						img: this.model.getImg(data.id),
						name: data.name
					});
				}
			});
			
			dd.addDisplay({
				type: 'mastery_container',
				// Expects: Array of Items
				success: function(data) {
					var tree, key;
					
					if (!Riot.isArray(Riot.QATool.MasteryApp.trees)) {
						Riot.QATool.MasteryApp.trees = [];
					}
					
					fn.$('#filter-bar, #righttool, #sorttool').addClass('ninja');
					
					Riot.QATool.MasteryApp.summoner = Riot.create('Riot.QATool.masteries.Summoner');
					Riot.QATool.MasteryApp.summoner.render($('#fullarea')[0]);
					
					Riot.QATool.MasteryApp.rendered = true;
					
					return '';
				}
			});
		},
		onDestroy: function () {
			Riot.QATool.MasteryApp.rendered = false;
			
			Riot.QATool.MasteryApp.summoner.destroy();
			
			Riot.QATool.MasteryApp.trees = [];
		}
	};
}());