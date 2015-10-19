/**
 * @class Riot.QATool.masteries.Item
 * @extends Riot.Component
 * A class used to represent a mastery. It facilitates basic interactions and rendering.
 */
Riot.define('Riot.QATool.masteries.Item', {
	extend: 'Riot.Component',

	baseId: 'mastery',
	baseClass: 'mastery',
	
	renderTpl: [
		'<div data-rg-name="mastery" data-rg-id="{{ dataId }}">',
			'<div id="{{ id }}-frame" class="frame"></div>',
			'<div id="{{ id }}-img" class="image">{{ img }}</div>',
			'<div id="{{ id }}-gray-img" class="gray-image">{{ grayImg }}</div>',
			'<div id="{{ id }}-points" class="points">0/{{ max }}</div>',
		'</div>'
	],
	
	childEls: {
		frame: 'frame',
		pointContainer: 'points'
	},

	//New Properties
	tipTpl: [
		'{{ img }}',
		'<div class="info{{ maxClass }}">',
			'<div class="name">{{ name }} &#151; {{ id }}</div>',
			'<div class="rank">{{ rank_ }} {{ rank }}/{{ max }}</div>',
			'<div class="description">{{ description }}</div>',
		'</div>'
	],
	
	/**
	 * @cfg {Object} data
	 * The data from DragonTail used to describe this mastery.
	 */
	/**
	 * @cfg {Number} tier
	 * The tier this mastery is located at within the tree.
	 */
	/**
	 * @cfg {Number} slot
	 * The slot this mastery is located at within the tree. This is a number between 0 and 3.
	 */
	/**
	 * @cfg {Riot.QATool.masteries.Tree} tree
	 * The tree this mastery belongs to.
	 */
	
	//Riot.Component Overrides
	init: function (config) {
		var me = this;
		
		me.addEvents({
			/**
			 * @event
			 * Triggered after a point is added.
			 * @param {Riot.QATool.masteries.Item} mastery The mastery a point was added to.
			 * @param {Number} points The current number of points in the mastery.
			 */
			pointadded: true,
			/**
			 * @event
			 * Triggered after a point is removed.
			 * @param {Riot.QATool.masteries.Item} mastery The mastery a point was removed from.
			 * @param {Number} points The current number of points in the mastery.
			 */
			pointremoved: true
		});
		
		me.callParent(arguments);
	},
	
	initComponent: function () {
		var me = this;
		
		me.points = 0;
		me.max = me.data.ranks;
		
		me.addClass([
			'left' + me.slot,
			'top' + me.tier,
			'mastery-empty'
		]);

		me.renderData = {
			slot: me.slot,
			tier: me.tier,
			dataId: me.data.id,
			img: me.img,
			grayImg: me.grayImg,
			max: me.max
		};
		
		me.callParent(arguments);
	},

	afterRender: function () {
		var me = this,
			prereq = me.getPrereq();
		
		me.frame.on('click', me.onClick, me);
		me.frame.on('contextmenu', me.onContextMenu, me);

		if (prereq) {
			prereq = me.tree.find(prereq);
			Riot.DDragon.fn.$(me.el.dom).append('<div class="prereq prereq-' + (me.tier - prereq.tier) + '"></div>');
		}
		
		me.callParent(arguments);
	},
	
	//New Methods
	/**
	 * @method
	 * Gets the id of the mastery.
	 * @return {Number} The id of the mastery.
	 */
	getDataId: function () {
		return this.data.id;
	},

	/**
	 * @method
	 * Gets the number of points currently in this mastery.
	 * @return {Number} The number of points in this mastery.
	 */
	getCurrent: function () {
		return this.points;
	},
	
	/**
	 * @method
	 * Gets any prereq this mastery has before it can be enabled.
	 * @return {String} The ID of a prereq if one exists. False if none is required.
	 */
	getPrereq: function () {
		var prereq = this.data.prereq;
		
		return (prereq === '0')? false : prereq;
	},
	
	/**
	 * @method
	 * Gets the tier of the mastery.
	 * @return {Number} The tier of the mastery.
	 */
	getTier: function () {
		return this.tier;
	},

	/**
	 *  @method
	 *  Gets the formatted tooltip text for the current mastery level.
	 *  @return {String} The html for the current tooltip.
	 */
	getTip: function () {
		var me = this,
			current = me.getCurrent(),
			index = current - 1,
			max = me.max,
			maxClass = '',
			description = [],
			requires = [],
			prereq;
		
		if (index < 0) {
			index = 0;
		}
		
		description.push(me.data.description[index]);
		
		if (current > 0 && current < max) {
			description = description.concat([
				'<div class="next">',
					'{{ nextRank_ }}<br/>',
					me.data.description[index + 1],
				'</div>'
			]);
		}
		
		if (current === max) {
			maxClass = ' maxed';
		}
		
		if (!me.tree.canAddPoint(me)) {
			maxClass = ' unavailable';
			
			prereq = me.getPrereq();
			
			requires.push('<div class="requires">');
			
			if (prereq) {
				prereq = me.tree.find(prereq);
				
				requires.push('Requires ' + prereq.max + ' points in ' + prereq.data.name + '.<br/>');
			}
			
			requires.push('Requires ' + (me.getTier() * 4) + ' points in ' + Riot.DDragon.fn.t('mastery' + me.tree.name) + '.');
			
			requires.push('</div>');
			
			description.unshift(requires.join(''));
		}
		
		return Riot.format(me.tipTpl, {
			img: me.img,
			name: me.data.name,
			id: me.data.id,
			description: description.join(''),
			rank: current,
			max: max,
			maxClass: maxClass,
			rank_: Riot.DDragon.fn.t('Rank_'),
			nextRank_: Riot.DDragon.fn.t('NextRank_')
		});
	},
	
	/**
	 * @method
	 * Checks to see if this mastery is maxed.
	 * @return {Boolean} Whether or not this mastery is maxed.
	 */
	isMaxed: function () {
		var me = this;
		
		return me.points === me.max;
	},

	/**
	 * @method
	 * Adds a point to this mastery. Triggers the {@link #pointadded} event.
	 */
	addPoint: function () {
		var me = this;

		if (me.isMaxed()) {
			return false;
		}

		if (!me.tree.canAddPoint(me)) {
			return false;
		}

		me.points = me.points + 1;

		me.updateDisplay();

		me.onAdd();

		me.fireEvent('pointadded', me, me.points);
	},
	
	/**
	 * @method
	 * Removes a point from this mastery. Triggers the {@link #pointremoved} event.
	 */
	removePoint: function () {
		var me = this;
		
		if (me.points === 0) {
			return false;
		}
		
		if (!me.tree.canRemovePoint(me)) {
			return false;
		}
		
		me.points = me.points - 1;
		
		me.updateDisplay();
		
		me.onRemove();
		
		me.fireEvent('pointremoved', me, me.points);
	},
	
	/**
	 * @method
	 * Updates the point display for this mastery.
	 */
	updateDisplay: function () {
		var me = this,
			classes = Riot.DDragon.controllers.cont1.classes.replace(/^\s+|\s+$/g,'').split(' ').join('.'),
			els;
		
		me.pointContainer.html(me.points + '/' + me.max);

		me.toggleClass({
			'mastery-maxed': me.isMaxed(),
			'mastery-empty': me.points === 0
		});

		els = Riot.query('.' + classes);

		Riot.each(els, function (el) {
			Riot.get(el).html(me.getTip());
		});
		//Riot.DDragon.controllers.cont1.redraw('get', me.data.id);
	},

	/**
	 * @method
	 * Marks the mastery as available.
	 */
	makeAvailable: function () {
		var me = this;

		me.addClass('mastery-available');
	},

	/**
	 * @method
	 * Marks the mastery as unavailable.
	 */
	makeUnavailable: function () {
		var me = this;

		if (me.points > 0) {
			return;
		}

		me.removeClass('mastery-available');
	},

	//Event Handlers
	onClick: function () {
		var me = this;

		me.addPoint();

		return false;
	},
	onContextMenu: function () {
		var me = this;

		me.removePoint();

		return false;
	},
	onAdd: function () {
		var me = this;

		Riot.DDragon.defaultPlayer.setMastery(me.data.id, me.points);
	},
	onRemove: function () {
		var me = this;

		Riot.DDragon.defaultPlayer.setMastery(me.data.id, me.points);
	}
});