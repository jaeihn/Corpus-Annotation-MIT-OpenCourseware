
function update_page(response) {
  	document.getElementById('search-result').innerHTML = "NEW";
}


function search()
{
	var form = document.getElementById("form");
	const formData = new FormData(form);
	const searchParams = new URLSearchParams(formData);
	const queryString = searchParams.toString();
//        alert(searchParams);
	xmlHttpRqst = new XMLHttpRequest( )
	xmlHttpRqst.onload = function(e) {update_page(xmlHttpRqst.response);} 
	xmlHttpRqst.open( "GET", "/search-by-title?" + searchParams);
	try {
		xmlHttpRqst.send( null );
	}
	catch(err)
	{
		alert(err);
	}
}
