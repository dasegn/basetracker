// Chosen init file

jQuery = jQuery ? jQuery : django.jQuery;
var $ = jQuery ? jQuery : django.jQuery;

jQuery(document).ready(function(){
	//jQuery(".chosen-select").chosen();
	setTimeout(function(){
    	//jQuery("select").not(".filtered").chosen();
    	jQuery(".chosen-select").chosen();
  	}, 500);
	// Tweak the CSS for any parent of a Chosen widget.
	setTimeout(function() {
		jQuery(".chosen-container").parents(".form-row").css({
		  "position": "relative",
		  "overflow": "visible"
		});
	}, 1000);  		
});
