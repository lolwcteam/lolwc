Riot.define('Riot.QATool.masteries.Tree', {
	extend: 'Riot.Component',
	
	baseClass: 'rg-mastery-trunk',
	
	renderTpl: [
		'<div class="title">',
			'{{ name }}: ',
			'<span id="{{ id }}-points" class="points">0</span>',
		'</div>'
	],
	
	childEls: {
		pointEl: 'points'
	},
	
	init: function () {
		var me = this;
		
		me.addEvents({
			pointadded: true,
			pointremoved: true,
			reset: true
		});
		
		me.masteries = [];
		
		me.callParent(arguments);
	},
	
	initComponent: function () {
		var me = this,
			tier, slot, tierLength, slotLength;
		
		for (tier = 0, tierLength = me.data.length; tier < tierLength; tier = tier + 1) {
			for (slot = 0, slotLength = me.data[tier].length; slot < slotLength; slot = slot + 1) {
				if (me.data[tier][slot]) {
					me.addMastery(me.data[tier][slot], slot, tier);
				}
			}
		}
		
		me.callParent(arguments);
	},
	
	addMastery: function (data, x, y) {
		var me = this,
			model = Riot.DDragon.useModel('mastery'),
			mastery;

		if (!data.ranks) {
			data = model.getFull(data.masteryId);
		}

		mastery = Riot.create('Riot.QATool.masteries.Item', {
			data: data,
			slot: x,
			tier: y,
			img: model.getImg(data.id),
			grayImg: model.getImg(data.id, { gray: true, classes: 'gray-img' }),
			tree: me
		});
		
		if (me.rendered) {
			mastery.render(me.el);
		}
		
		mastery.on('pointadded', me.onPointAdded, me);
		mastery.on('pointremoved', me.onPointRemoved, me);
		
		me.masteries.push(mastery);
	},
	
	onPointAdded: function () {
		var me = this;
		
		me.points = me.points + 1;
		
		me.updateTiers();
		me.updateDisplay();
		
		me.fireEvent('pointadded', me, me.points);
	},
	
	onPointRemoved: function () {
		var me = this;
		
		me.points = me.points - 1;
		
		me.updateTiers();
		me.updateDisplay();
		
		me.fireEvent('pointremoved', me, me.points);
	},
	
	updateDisplay: function () {
		var me = this;
		
		me.pointEl.html(me.getCurrent());
	},
	
	updateTiers: function () {
		var me = this;
		
		me.each(function (mastery) {
			if (me.canAddPoint(mastery)) {
				mastery.makeAvailable();
			} else {
				mastery.makeUnavailable();
			}
		});
	},
	
	afterRender: function () {
		var me = this,
			i, length;
		
		for (i = 0, length = me.masteries.length; i < length; i = i + 1) {
			me.masteries[i].render(me.el);
		}
		
		me.callParent(arguments);
	},
	
	initRenderData: function () {
		return this.callParent([{
			name: Riot.DDragon.fn.t('mastery' + this.name).toUpperCase()
		}]);
	},
	
	find: function (id) {
		var me = this,
			i, length,
			masteries = me.masteries;
		
		for (i = 0, length = masteries.length; i < length; i = i + 1) {
			if (masteries[i].getDataId() === id) {
				return masteries[i];
			}
		}
		
		return false;
	},
	
	canAddPoint: function (mastery) {
		var me = this,
			dependency,
			i, length;
		
		if (typeof mastery === 'string') {
			mastery = me.find(mastery);
		}
		
		if (me.getCurrent() < (mastery.tier * 4)) {
			return false;
		}
		
		if (!me.summoner.canAddPoint()) {
			return false;
		}
		
		dependency = me.getDependency(mastery.getDataId());
		
		if (dependency && !dependency.isMaxed()) {
			return false;
		}
		
		return true;
	},
	
	canRemovePoint: function (mastery) {
		var me = this,
			dependant,
			i, length;
		
		if (typeof mastery === 'string') {
			mastery = me.find(mastery);
		}
		
		dependant = me.getDependant(mastery.getDataId());
		
		if (dependant && dependant.getCurrent() > 0) {
			return false;
		}
		
		if (!me.checkTier(null, {
			tier: mastery.getTier(),
			value: -1
		})) {
			return false;
		}
		
		return true;
	},
	
	getDependant: function (id) {
		var me = this,
			masteries = me.masteries,
			i, length;
		
		for (i = 0, length = masteries.length; i < length; i = i + 1) {
			if (masteries[i].getPrereq() === id) {
				return masteries[i];
			}
		}
		
		return null;
	},
	
	getDependency: function (id) {
		var me = this,
			mastery = id;
		
		if (typeof mastery === 'string') {
			mastery = me.find(mastery);
		}
		
		if (mastery.getPrereq()) {
			return me.find(mastery.getPrereq());
		}
		
		return null;
	},
	
	checkTier: function (tier, modifier) {
		var me = this,
			sum = 0,
			i, length;
		
		if (typeof tier !== 'number') {
			for (i = 0, length = me.getHighestTier(); i < length; i = i + 1) {
				if (!me.checkTier(i, modifier)) {
					return false;
				}
			}
			
			return true;
		}
		
		for (i = tier - 1; i >= 0; i = i - 1) {
			sum = sum + me.getCurrent(i);
			
			if (modifier.tier === i) {
				sum = sum + modifier.value;
			}
		}
		
		return sum >= (tier * 4);
	},
	
	getCurrent: function (tier) {
		var me = this,
			masteries = me.masteries,
			total = 0;
		
		if (tier !== undefined) {
			masteries = me.getTier(tier);
		}
		
		Riot.each(masteries, function (mastery) {
			total = total + mastery.getCurrent();
		});
		
		return  total;
	},
	
	getTier: function (tier) {
		var me = this,
			masteries = [];
		
		me.each(function (mastery) {
			if (mastery.getTier() === tier) {
				masteries.push(mastery);
			}
		});
		
		return masteries;
	},
	
	getHighestTier: function () {
		var me = this
			max = 0;
		
		me.each(function (mastery) {
			if (mastery.getTier() > max && mastery.getCurrent() > 0) {
				max = mastery.getTier();
			}
		});
		
		return max + 1;
	},
	
	each: function (fn) {
		var me = this;
		
		Riot.each(me.masteries, fn);
	},
	
	onDestroy: function () {
		var me = this;
		
		me.each(function (item) {
			item.destroy();
		});
		
		me.callParent(arguments);
	}
});