$(function(){
	$("#search").bind("change keyup input click", function() {
		if(this.value.length >=2){
			var search = $("#search").val();
			$.ajax({
				type: "POST",
				url: "search.php",
				data: {"search": search},
				cache: false,                                 
				success: function(response){
					$("#resSearch").html(response);
				}
			});
			$(".hideme").fadeOut();
			return false;
		}else{
			$(".hideme").fadeIn();
		}
	});
});