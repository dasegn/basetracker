// Chosen init file
(function($, undefined){
	jQuery(document).ready(function(){
		//jQuery(".chosen-select").chosen();
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
			jQuery('.add-row a').bind('click', function(e) { 
				var elems = [];
				jQuery(this).closest(".add-row").siblings().each(function() {
				//  this should be the dynamic set (dynamic-inlinemodelname_set)
					if ( jQuery(this).attr('class').match(/\bdynamic\-.*_set\b/) ) {				  	
						var select = jQuery(this).find("select.chosen-select");
						select.each(function(){
							elems.push(jQuery(this));
						});			
						//  undo chosen
					}
				});
				chosenReset(elems);		
			 });	
		}, 1000); 
	});

function chosenReset(obj){	
	jQuery.each(obj, function(){
		console.log(jQuery(this));
		jQuery(this).removeAttr('style');
		jQuery(this).parents("td").find(".chosen-container").remove();
		//jQuery(this).chosen('destroy');
		jQuery(this).chosen();
	});			

}

})((typeof window.django != 'undefined') ? django.jQuery : jQuery);