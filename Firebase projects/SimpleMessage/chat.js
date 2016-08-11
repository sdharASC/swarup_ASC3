var database = firebase.database().ref();

function sendMessage() {
	var firstName = $('#firstName').val();
	var lastName  = $('#lastName').val();
	var msg 	  = $('#msg').val();
	database.push({
		'firstName' : firstName,
		'lastName'  : lastName,
		'msg'		: msg,
		'test'		: [0, 1, 2, 3]
	});
	$('#firstName').val("");
	$('#lastName').val("");
	$('#msg').val("");
}

database.on('child_added', function(dataRow) {
	var row = dataRow.val();
	$('#messageBoard').append('<p>' + "<h2> Name: </h2>" + row.lastName + ", " + row.firstName + "<h2>Message</h2>"+row.msg + '<p>');
});

