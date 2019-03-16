$(document).ready(function () {
    $("#btn").one("click",
        function () {
            $.ajax({
                type: "get",
                url: "/note_info/",
                dataType: "json",
                success:
                    function (data, status) {
                    let d = data["data"];
                    console.log(d);
                    for (let i = 0;i<d.length;i++){
                        let res = d[i];
                        console.log(res);
                        $('.add').append("<li><a>"+res.Note_name+"</a></li>")
                    }
                }
            })
        });
});
    // document.getElementById("btn").onclick =
    //     function () {
    //         $.ajax({
    //             type: "get",
    //             url: "/note_info/",
    //             dataType: "json",
    //             success:
    //                 function (data, status) {
    //                 let d = data["data"];
    //                 console.log(d);
    //                 for (let i = 0;i<d.length;i++){
    //                     let res = d[i];
    //                     console.log(res);
    //                     $('.add').append("<li><a>"+res.Note_name+"</a></li>")
    //                 }
    //             }
    //         })
    //     }

