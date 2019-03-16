$(document).ready(function () {
    //获取当前页面的信息
    let  currentURL = window.location;
    //点击上一页
    $(".page .previous").one("click",
        function () {
        //分割url字符串
        let x = currentURL.href.split("/");
        //x[4]为当前页面的页码数
        let page = x[4]-1;
        //判断是否为第一页
        if (page !== 1) {
            console.log("没有上个页面")
        }else {
            window.location.href="/study_notes/"+page+"/";
        }
    });

    $(".page .next").one("click",
        function () {
            //获取page下面的a标签的个数
            let lang_a = $(".page").find("a").length;
            //得到页码数
            let lang = lang_a - 2;
            let x = currentURL.href.split("/");
            //判断当前页面是否有页码，以及是否为最后一页
            if (x[4] === ''){
                window.location.href="/study_notes/2/";
            } else if (parseInt(x[4]) === lang) {
                console.log("没有下一页")
            } else {
                let page = parseInt(x[4])+1;
                window.location.href="/study_notes/"+page+"/";
            }
    });
});