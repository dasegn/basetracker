// Chosen init file
(function($, undefined){
	jQuery(document).ready(function(){
		setTimeout(function(){
			jQuery(".chosen-select").chosen();
		}, 500);		

		// Tweak the CSS for any parent of a Chosen widget.
		setTimeout(function() {
			jQuery(".chosen-container").parents(".grp-row").css({
			  "position": "relative",
			  "overflow": "visible"
			});
		}, 1000);

		setTimeout(function(){
			jQuery('.grp-row a.grp-add-handler').on('click', function(e) { 
				jQuery(this).closest(".grp-module").siblings('.grp-table').children('.grp-module').each(function() {
				//  this should be the dynamic set (dynamic-inlinemodelname_set)
					//if ( jQuery(this).attr('class').match(/\bdynamic\-.*_set\b/) ) {				  	
					if ( jQuery(this).attr('class').match(/grp-dynamic-form/) ) {				  	
						var select = jQuery(this).find("select.chosen-select");
						jQuery.each(select, function(){
							jQuery(this).parent(".grp-td").find(".chosen-container").remove();							
							jQuery(this).chosen('destroy');
							jQuery(this).chosen();
						});		
					}
				});
			 });	
		}, 1000); 
	});

})((typeof window.django != 'undefined') ? django.jQuery : jQuery);