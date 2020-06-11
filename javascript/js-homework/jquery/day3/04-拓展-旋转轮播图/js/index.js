/**
 * Created by Lenovo on 2017/11/23.
 */
$(window).load(function() {

    var arrOfJson = [{ //  1
            width: 400,
            top: 70,
            left: 50,
            opacity: 0.2,
            "z-index": 2
        },
        { // 2
            width: 600,
            top: 120,
            left: 0,
            opacity: 0.8,
            "z-index": 3
        },
        { // 3
            width: 800,
            top: 100,
            left: 200,
            opacity: 1,
            "z-index": 4
        },
        { // 4
            width: 600,
            top: 120,
            left: 600,
            opacity: 0.8,
            "z-index": 3
        },
        { //5
            width: 400,
            top: 70,
            left: 750,
            opacity: 0.2,
            "z-index": 2
        }
    ];

    $(".slide li").each(function(index, ele) {
        $(ele).css("z-index", arrOfJson[index]["z-index"])
        $(ele).animate(arrOfJson[index], 1000);
    });


    $("#wrap").hover(function() {
        $("#arrow").fadeTo(100, 1);
    }, function() {
        $("#arrow").fadeTo(100, 0);
    });

    //需求2: 点击右侧按钮，删除数组中最后一个，添加到数组的最前面;
    $(".next").click(function() {
        if (bool == false) {
            return;
        }
        //如果是true才能走到这，走到这里，直接改为false，下次就不能点击了
        bool = false;

        //删除数组中最后一个，添加到数组的最前面;
        var last = arrOfJson.pop();
        arrOfJson.unshift(last);

        //按照新数组的元素排布，在此执行一次页面上的li;
        $("#slide li").each(function(index, ele) {
            //bug: 层级没有第一时间到达;
            $(ele).css("z-index", arrOfJson[index]["z-index"])
            $(ele).animate(arrOfJson[index], 1000, function() {
                //执行回调函数的时候，就是全部属性执行到目标位置的时候
                bool = true;
            });
        });
    });

    //需求3: 点击左侧按钮，删除数组中第一个，添加到数组的最后面;
    $(".prev").click(function() {
        //删除数组中第一个，添加到数组的最后面;
        var first = arrOfJson.shift();
        arrOfJson.push(first);
        //按照新数组的元素排布，在此执行一次页面上的li;
        $("#slide li").each(function(index, ele) {
            //bug: 层级没有第一时间到达;
            $(ele).css("z-index", arrOfJson[index]["z-index"])
            $(ele).animate(arrOfJson[index], 1000);
        });
    });

});