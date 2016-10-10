$(function() {
        $(".flash .con ul li").click(function(){
            $(this).stop().animate({width:"605px"},300).siblings().stop().animate({width:"46px"},300)
        });


	$('.sidebar .widget ul li:first-child').addClass('first');
	$('.footer-nav ul li:first-child').addClass('first');
var qc=$(".post-inner h2").find("a").attr("href");
var nc=$(".item").find("a[href='"+qc+"']");
if(nc!=null){
nc.addClass("current");
$(".flash .con ul li").animate({width:"46px"},300);
nc.parent().parent().parent().animate({width:"605px"},300);
}
});

(function(){ var bp = document.createElement('script'); bp.src = '//push.zhanzhang.baidu.com/push.js'; var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(bp, s); })();
