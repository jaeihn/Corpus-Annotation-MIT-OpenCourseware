

function update_page(response) {
  	document.getElementById('flex-container').innerHTML = response;
}


function addDiv()
{
	var form = document.getElementById("form");
	const formData = new FormData(form);
	const searchParams = new URLSearchParams(formData);
	const queryString = searchParams.toString();
        alert(searchParams);
	xmlHttpRqst = new XMLHttpRequest( )
	xmlHttpRqst.onload = function(e) {update_page(xmlHttpRqst.response);} 
	xmlHttpRqst.open( "GET", "/pos?" + queryString);
	try {
		xmlHttpRqst.send( null );
	}
	catch(err)
	{
		alert(err);
	}
}
