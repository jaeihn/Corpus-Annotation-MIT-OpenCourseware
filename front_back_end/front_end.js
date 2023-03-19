

function checkHappy()
{
     var checkbox = document.getElementById("happycheckbox");
     alert(checkbox.checked);
     if (checkbox.checked == false) {
        alert("You didn't say you were happy! HUH?");
    } 
    else {
	var form = document.getElementById("form");
        form.submit();
    }
}

function update_page(response) {
  	document.getElementById('search-result').innerHTML = "NEW";
}


function search()
{
	var form = document.getElementById("form");
	const formData = new FormData(form);
	const searchParams = new URLSearchParams(formData);
	const queryString = searchParams.toString();
        alert(searchParams);
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

function turnGreen() {
   var thing = document.getElementById("toturngreen");
   thing.setAttribute("class", "cell");
   thing.innerHTML = "I am!";
}
