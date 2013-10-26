/*

	jQuery - External Links
	Created by Andrea Cima Serniotti - http://www.madeincima.eu

*/


$(document).ready(function () {
	
	   // ---- FAQs ---------------------------------------------------------------------------------------------------------------
		
		$('.faqs dd').hide(); // Hide all DDs inside .faqs
		$('.faqs dt').hover(function(){$(this).addClass('hover')},function(){$(this).removeClass('hover')}).click(function(){ // Add class "hover" on dt when hover
		$(this).next().slideToggle('normal'); // Toggle dd when the respective dt is clicked
		}); 
	
});