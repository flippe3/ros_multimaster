function set_ip(socket, ip) {
    $.getJSON('/_set_ip', {
        select_ip: ip,
	select_socket: socket
    }, function(data) {
        $("#selected_ip").text(data.result);
    });
    return false;    
}

function set_topic(topic) {
    $.getJSON('/_set_topic', {
        select_topic: topic
    }, function(data) {
        $("#selected_topic").text(data.result);
    });
    return false;    
}
function refresh_ros_topics() {
    $.getJSON('/_refresh_topics', {
    }, function(data){ 
	//Cleans up old connections
	var conn = document.getElementById("li_topic");
	while (conn){
	    conn.parentNode.removeChild(conn);
	    conn = document.getElementById("li_topic");
	}
	data.result.forEach(function(topics) {
	    var li = document.createElement("li");
	    li.className = "list-group-item";
	    li.id = "li_topic";
	    
	    var text = document.createElement("text");
	    text.innerHTML = topics;

	    var select_btn = document.createElement("button");
	    select_btn.className = "btn btn-outline-primary float-right pt-0 pb-0";
	    select_btn.innerHTML = "Select";
	    select_btn.onclick= function () { set_topic(topics); };
	    select_btn.name = "selected_topic";

	    text.appendChild(select_btn);
	    li.appendChild(text);

	    document.getElementById("ros_topics_pos").appendChild(li);
	});
        $("#topics").text(data.result);
    });
    return false;    
}

function get_topic_data() {
    $.getJSON('/_get_topic_data', {
    }, function(data){
	console.log(data.result);
	var params = document.getElementById("li_param");
	while (params){
	    params.parentNode.removeChild(params);
	    params = document.getElementById("li_param");
	}


	data.result.forEach(function(params) {
	    var li = document.createElement("li");
	    li.className = "list-group-item";
	    li.id = "li_param";
	    
	    var text = document.createElement("text");
	    text.innerHTML = params;

	    var select_btn = document.createElement("button");
	    select_btn.className = "btn btn-outline-primary float-right pt-0 pb-0";
	    select_btn.innerHTML = "Select";
	    //select_btn.onclick= function () { set_topic(topics); };
	    select_btn.name = "selected_param";

	    text.appendChild(select_btn);
	    li.appendChild(text);

	    document.getElementById("bandwidth").appendChild(li);
	});
	//$("#bw").text(data.result);
        //$("#topics").text(data.result);
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

	for (let i = 0; i < data.ips.length; i++){
	    var li = document.createElement("li");
	    li.className = "list-group-item";
	    li.id = "li_connection";
	    
	    var text = document.createElement("text");
	    text.innerHTML = data.ips[i];

	    var select_btn = document.createElement("button");
	    select_btn.innerHTML = "Select"
	    select_btn.className = "btn btn-outline-primary float-right pt-0 pb-0";
	    select_btn.onclick= function () { set_ip(data.sockets[i], data.ips[i]); };
	    select_btn.name = "selected_ip";
	    select_btn.id = data.sockets[i];
	    
	    text.appendChild(select_btn);
	    li.appendChild(text);

	    document.getElementById("connection_pos").appendChild(li);
	}
    });
    return false;    
}

