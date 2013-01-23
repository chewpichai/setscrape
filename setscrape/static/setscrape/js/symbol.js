$(function() {
    var symbol = $('#symbol-graph-wrapper').attr('symbol');
    $.getJSON('/api/?method=get_stock&symbol=' + encodeURIComponent(symbol), function(data) {
        // create the chart
    	chart = new Highcharts.StockChart({
			chart : {
				renderTo : 'symbol-graph-wrapper'
			},

			rangeSelector : {
				selected : 1
			},

			series : [{
				type : 'candlestick',
				name : data.name + ' Stock Price',
				data : data.data,
				dataGrouping : {
					units : [
						['week', // unit name
						[1] // allowed multiples
					], [
						'month', 
						[1, 2, 3, 4, 6]]
					]
				}
			}]
		});
	});
});