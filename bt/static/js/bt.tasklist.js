// Chosen init file
(function($){
	jQuery(document).ready(function(){
		jQuery.datepicker.regional['es'] = {
			 closeText: 'Cerrar',
			 prevText: '<Ant',
			 nextText: 'Sig>',
			 currentText: 'Hoy',
			 monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
			 monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
			 dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
			 dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
			 dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
			 weekHeader: 'Sm',
			 dateFormat: 'dd/mm/yy',
			 firstDay: 1,
			 isRTL: false,
			 showMonthAfterYear: false,
			 yearSuffix: ''
		 };		
		jQuery.datepicker.setDefaults( jQuery.datepicker.regional[ "es" ] );

		jQuery('.weekpicker').weekpicker({
			firstDay: 1,
			weekLength: 7,
			showWeek: true,
			startField: jQuery('.startField'),
			endField: jQuery('.endField'),
			dateFormat: 'yy-mm-dd',
	        onSelect: function(dateText, inst) {
	        	seldate = $.datepicker.parseDate( "yy-mm-dd", dateText);	        	
	            var weekNumber = jQuery.datepicker.iso8601Week(seldate);	            
	            var year = getRealYear(jQuery(this).datepicker('getDate'));	            
	            jQuery('.listName').val("Semana " + weekNumber + ' ' + year);	            
	        }			
		});

		function getRealYear(dates) {
			var checkDate = new Date(dates.getTime());
			// Find Thursday of this week starting on Sunday
			checkDate.setDate(checkDate.getDate() + 4 - (checkDate.getDay()));
			var time = checkDate.getTime();
			checkDate.setMonth(0); // Compare with Jan 1
			checkDate.setDate(1);
			//return (Math.floor(Math.round((time - checkDate) / 86400000) / 7) + 1);
			return checkDate.getFullYear();
		}


	});
})((typeof window.django != 'undefined') ? django.jQuery : jQuery);