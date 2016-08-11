function grabData() {
	var name = $("#title").val();

	$.ajax({
		url: 'http://www.omdbapi.com/?t=' + name,
		success: function (result) {
			print_result(result);
		}
	});
}

function print_result(obj) {
	$("#content").text("");

	for(var i in obj){
		$("#content").append('<p>' + i + ': ' + obj[i] + '</p>');
	}
}

$('#submit').click(function() {
	grabData();
});
