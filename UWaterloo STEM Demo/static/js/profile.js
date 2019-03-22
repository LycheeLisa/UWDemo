function clusterview(val){
	$.post("/clusterview",
	{
		data: JSON.stringify(val),
	},
	function(response) {
					$("#profile").html(response);

				},
);
$([document.documentElement, document.body]).animate({
	scrollTop: $("#profile").offset().top
}, 2000);

};
