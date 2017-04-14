
$(".ip_button").click(function(e){
	e.preventDefault();
	var id = $(this).attr("data-id");
	var ip = $(this).attr("data-ip");
	reserveIp(id, ip, $(this).parent());
})

	function reserveIp(id, ip, el){$.ajax({
		type:"GET",
		url:"/delete/"+id,
		success: function(response){
			if(response){
				el.hide();
				alert("You claimed " + ip)
			}
		},
		error: function(a, b, c){
			alert("There was an error when trying to claim this IP address")
		}
	})}