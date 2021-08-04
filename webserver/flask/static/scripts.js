function set_ip(ip) {
    $.getJSON('/_set_ip', {
        select_ip: ip
    }, function(data) {
        $("#selected_ip").text(data.result);
    });
    return false;    
}

function refresh_connections() {
    $.getJSON('/_refresh_connections', {
    }, function(data){ 
	//Cleans up old connections
	var conn = document.getElementById("li_connection");
	while (conn){
	    conn.parentNode.removeChild(conn);
	    conn = document.getElementById("li_connection");
	}

	data.result.forEach(function(ip) {
	    var li = document.createElement("li");
	    li.className = "list-group-item";
	    li.id = "li_connection";
	    
	    var text = document.createElement("text");
	    text.innerHTML = ip;

	    var select_btn = document.createElement("button");
	    select_btn.innerHTML = "Select"
	    select_btn.className = "btn btn-outline-primary float-right pt-0 pb-0";
	    select_btn.onclick= function () { set_ip(ip); };
	    select_btn.name = "selected_ip";

	    text.appendChild(select_btn);
	    li.appendChild(text);

	    document.getElementById("connection_pos").appendChild(li);
	});
        $("#connections").text(data.result);
    });
    return false;    
}
