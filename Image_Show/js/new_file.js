$("#piclist span").click(function() {
	//给9张图片添加点击的触发事件
	var index = $(this).index();
	alert("Span被点击。。。" + index);

	//跟换图片
	var $imgs = $("#showimg span img");
	alert("图片的个数：" + $imgs.length);
	//通过For循环替换所有图片
	for(var i = 0; i < $imgs.length; i++) {
		//获取一个动态的图片路径
		var imgurl = "img/show/" + index + "/" + (i + 1) + ".jpg";
		//提取$imgs中的每一个img标签
		$imgs.eq(i).attr("src", imgurl);

	}

	//让遮光布显示出来，图片，按钮
	//	$("#show").show();
	//渐入效果 ;时间单位：毫秒 1000 = 1秒
	$("#show").fadeIn(500);
	$("#showimg").fadeIn(500);
	$(".btn").fadeIn(500);

});

//退出效果
$("#show").click(function() {
	//渐入效果 ;时间单位：毫秒 1000 = 1秒
	$("#show").fadeOut(500);
	$("#showimg").fadeOut(500);
	$(".btn").fadeOut(500);
})

//给下一张按钮添加监听
$(".btn_02").click(function() {
	//	alert("下一张")
	//left:0px
	$("#showimg span:last-child").animate({
		"left": "650px"
	}, 1000, function() {
		$(this).animate({
			"left": "0px"
		}, 1000);
		//prepend函数把指定元素插入到但前元素相对列表中开始位置；
		$("#showimg").prepend($(this));
	})
});

//给下一张按钮添加监听
$(".btn_01").click(function() {
	$("#showimg span:first-child").animate({
		"left": "-650px"
	}, 1000, function() {
		$(this).animate({
			"left": "0px"
		}, 1000);
		//prepend函数把指定元素插入到但前元素相对列表中结束位置；
		$("#showimg").append($(this));
	})
});

//自动播放
function abc() {
	$("#showimg span:last-child").animate({
		"left": "650px"
	}, 1000, function() {
		$(this).animate({
			"left": "0px"
		}, 1000);
		//prepend函数把指定元素插入到但前元素相对列表中开始位置；
		$("#showimg").prepend($(this));
	})
}

//定时器调用:第一个参数：函数名称 ；第二个：间隔时间
setInterval(abc,4000);




//函数的创建
//function 函数名(){
//	
//}