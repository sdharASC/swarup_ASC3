var search = $("#search");
var resultDiv = $('#results');
var time = 0;
var limit = 2;
var timer = setInterval(function() {time++}, 1000);
var lichessURL = "https://en.lichess.org/api/user/";

function print_user_data(data) {
	$("#username").text("");
	$("#title").text("");
	$("#online").text("");
	$("#engine").text("");
	$("#perfs").text("");
	$("#url").text("");
	$("#nbFollowers").text("");

	for(var i in data){
		if (i == 'username'){
			$("#username").text(data[i]);
		}
		else if (i == 'title'){
			$("#title").text(data[i]);
		}
		else if (i == 'online'){
			if(data[i] == false){
				$("#online").text("Offline");
			}else{
				$("#online").text("Online");
			}
		}
		else if (i == 'engine'){
			if(data[i] == false){
				$("#engine").text("No");
			}else if(data[i]==true){
				$("#engine").text("Yes");
			}
			else{
				$("#engine").text("N/A");
			}
		}
		else if(i == 'profile'){
			if(data[i]["bio"]){
				$("#profile").append("<p> Bio: " + data[i]['bio'] + " </p>");
			}
			if(data[i]["firstName"]){
				$("#profile").append("<p> First Name: " + data[i]['firstName'] + " </p>");
			}
			if(data[i]["lastName"]){
				$("#profile").append("<p> Last Name: " + data[i]['lastName'] + " </p>");	
			}
			if(!data[i]["bio"] && !data[i]["firstName"] && !data[i]["lastName"]){
				$("#profile").append("<p>N/A </p>");	
			}
		}
		else if(i == 'perfs'){
			getGameInfo(data[i]);
		}
		else if(i == 'url'){
			$("#url").append("<a href='"+ data[i] +"'> Profile Page </a>").css("text-decoration", "none");
		}
		else if(i == 'nbFollowers'){
			$("#nbFollowers").append(data.nbFollowers);
		}
		else{
		}
	}
	if(data.username){
		var apiUrl = lichessURL + data.username + "games?nb=20";
		$.ajax({
			url: apiUrl,
			dataType:'jsonp',
			jsonp:'callback',
			success: function(result) {
				
			}
		});
	}
}

function getGameInfo(data) {
	for(var i in data){
		$("#perfs").append("<strong>"+i+"</strong><br> <i>Number of games: </i>" + data[i].games + "<br>");
		$("#perfs").append("<i>Rating: </i>" + data[i].rating + "<br>");
		$("#perfs").append("<i>Rating change over the last 12 games: </i>" + data[i].prog + "<br>");
	}
}

function userInfo() {
	if(time >= limit){
		$.ajax({
			url: lichessURL + search.val(),
			dataType:'jsonp',
			jsonp:'callback',
			success: function(result) {
				print_user_data(result);
			}
		});
		time = 0;
	}
}

// add click to the button
$("#submit").click(function() {
	if(search.val() != ''){
		userInfo();
	}
});