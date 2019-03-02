
function updateImg(){
//	alert("==========")
	$("#uls ul li:last-child").animate({"opacity":"0"},1000,function(){
			$("#uls ul").prepend($(this));
		$(this).animate({"opacity":"1"},1000);
	
	});
}
//定时器调用
setInterval(updateImg,3000);
