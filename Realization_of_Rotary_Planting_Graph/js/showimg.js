$(".piclist span").click(function(){
	//要触发的代码
	//获去点击的是哪个span
	var index = $(this).index();
	//alert("["+index+"]图片被点击");
	//让隐藏的标签显示
	//$("#show").show();
	//渐入渐出效果：时间单位为毫秒
	$("#show").fadeIn(1000);
	$("#showimg").fadeIn(1000);
	$(".btn").fadeIn(1000);
	//获去5张图片的标签
	var $img = $("#showimg span img");
	//alert("照片个数："+$img.length);
	//通过循环语句更换5张图片
	for(var i=0;i<$img.length;i++){
		//动态图片路径
		var imgurl = "img/show/"+index+"/"+(i+1)+".jpg"
		//扎到每个img标签
		$img.eq(i).attr("src",imgurl)
	}
});
//给遮光布设置点击事件:退出事件
$("#show").click(function(){
	$("#show").fadeOut(1000);
	$("#showimg").fadeOut(1000);
	$(".btn").fadeOut(1000);
});

//点击下一张
$(".btn_02").click(function(){
	//alert("下一张 切换中");
	$("#showimg span:last-child").animate({"left":"650px"},500,function(){
		$(this).animate({"left":"0px"},1500);
		//prepend函数：将制定元素插入到当前元素列表中开始的位置
		$("#showimg").prepend($(this));
	})
})

//点击上一张
$(".btn_01").click(function(){
	//alert("下一张 切换中");
	$("#showimg span:first-child").animate({"left":"-650px"},500,function(){
		$(this).animate({"left":"0px"},1500);
		//append函数：将制定元素插入到当前元素列表中末尾的位置
		$("#showimg").append($(this));
	})
})

//浮动监听-鼠标接触一个按钮另一个消失
$(".btn_02").hover(function(){
	$(".btn_01").css("display","none")
},function(){
	$(".btn_01").css("display","block")
})

$(".btn_01").hover(function(){
	$(".btn_02").css("display","none")
},function(){
	$(".btn_02").css("display","block")
})
//连连看
/*
$(".piclist span").click(function(){
	//点中间的开始
	var index = $(this).index();
	if(index==4){
		alert("店家")
		//产生随机数
		min = 20
		max = 40
		var ran = parseInt(Math.random()*(max-min+1)+min,10);
		for(var i=0;i<ran;i++){
			$(".piclist span").eq(i).css("background","red");
			setTimeout(function(){alert("Hello")},1000*(i+1));
			$(".piclist span").eq(i).css("background","white");
		}
	}
})
*/

