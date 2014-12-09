// Chosen init file
(function($){
	jQuery(document).ready(function(){
		var month_names = django.catalog["January February March April May June July August September October November December"];
		var day_names = django.catalog["S M T W T F S"];
		
		jQuery.datepicker.setDefaults( jQuery.datepicker.regional[ "es" ] );
		jQuery('.weekpicker').weekpicker({
			firstDay: 1,
			weekLength: 7,
			//calculateWeek: myWeekCalc,
			startField: jQuery('.startField'),
			endField: jQuery('.endField'),
			dateFormat: 'yy-mm-dd',
			monthNames: month_names.split(" "),
			dayNamesMin: day_names.split(" "),
	        onSelect: function(dateText, inst) {
	            var weekNumber = jQuery.datepicker.iso8601Week(new Date(dateText));
	            console.log(weekNumber);
	            console.log(jQuery.datepicker.formatDate('D', new Date(dateText)));
	            var year = jQuery(this).datepicker('getDate').getFullYear();
	            jQuery('.listName').val("Semana " + weekNumber + ' ' + year);
	            
	        }			
		});
	});
})((typeof window.django != 'undefined') ? django.jQuery : jQuery);