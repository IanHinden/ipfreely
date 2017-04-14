alert("This is a test");

$(‘.ip-claim-link’).click(function(e){
e.preventDefault();
claimIP($(this).text());
});

$.ajax({

url: ‘localhost/claimip?address=‘ + ip,
type: ‘GET’,
success: function(response){
    alert(‘SUCCESS!’);
},
error: function(x,y,z){
}
