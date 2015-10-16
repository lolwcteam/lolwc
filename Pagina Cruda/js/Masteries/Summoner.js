Riot.define('Riot.QATool.masteries.Summoner', {
	extend: 'Riot.Component',
	
	baseClass: 'rg-display-mastery_container',
	
	afterRender: function () {
		var me = this,
			tree,
			model = Riot.DDragon.useModel('mastery'),
			i;
		
		me.trees = [];
		
		me.addClass('masterytree');
		
		me.el.setStyle('background', 'url(\'' + Riot.DDragon.m.cdn + 'img/mastery/masteryback.jpg\')');
		
		for (var key in model.tree) {
			if (model.tree.hasOwnProperty(key)) {
				tree = Riot.create('Riot.QATool.masteries.Tree', {
					data: model.tree[key],
					summoner: me,
					name: key
				});
				
				tree.on('pointadded', me.onPointAdded, me);
				tree.on('pointremoved', me.onPointRemoved, me);
				
				tree.render(me.el);
				
				me.trees.push(tree);
			}
		}
		
		for (i = 0; i < 3; i = i + 1) {
			me.trees[i].updateTiers();
		}
	},
	
	onDestroy: function () {
		var me = this,
			i;
		
		for (i = 0; i < 3; i = i + 1) {
			me.trees[i].destroy();
		}
		
		me.callParent(arguments);
	},
	
	onPointAdded: function () {
		var me = this;
		
		if (me.getCurrent() === 30) {
			me.addClass('masterytree-maxed');

			for (i = 0; i < 3; i = i + 1) {
				me.trees[i].updateTiers();
			}
		}
	},
	
	onPointRemoved: function () {
		var me = this;

		me.removeClass('masterytree-maxed');

		if (me.getCurrent() === 29) {
			for (i = 0; i < 3; i = i + 1) {
				me.trees[i].updateTiers();
			}
		}
	},
	
	getCurrent: function () {
		var me = this,
			total = 0,
			i;
		
		for (i = 0; i < 3; i = i + 1) {
			total = total + me.trees[i].getCurrent();
		}
		
		return total;
	},
	
	findMastery: function (id) {
		var me = this,
			mastery, i;
			
		for (i = 0; i < 3; i = i + 1) {
			mastery = me.trees[i].find(id);
			
			if (mastery) {
				return mastery;
			}
		}
	},
	
	canAddPoint: function () {
		return this.getCurrent() < 30;
	}
});