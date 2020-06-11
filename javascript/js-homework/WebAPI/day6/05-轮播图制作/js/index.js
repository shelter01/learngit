window.addEventListener('load', function() {
    var arrow_l = document.querySelector('.arrow-l');
    var arrow_r = document.querySelector('.arrow-r');
    var focus = document.querySelector('.focus');
    //左右框的显示与隐藏
    focus.addEventListener('mouseenter', function() {
        arrow_l.style.display = 'block';
        arrow_r.style.display = 'block';
    });
    focus.addEventListener('mouseleave', function() {
        arrow_l.style.display = 'none';
        arrow_r.style.display = 'none';
    });
    //动态生成下排小圆点
    var ul = focus.querySelector('ul');
    var ol = focus.querySelector('.circle');
    for (var i = 0; i < ul.children.length; i++) {
        var li = document.createElement('li');
        li.setAttribute('index', i);
        ol.appendChild(li);
        li.addEventListener('click', function() {
            for (var j = 0; j < ol.children.length; j++) {
                ol.children[j].className = '';
            }
            this.className = 'current';
            //点击圆点，图片跟着移动
            var index = this.getAttribute('index');
            num = index;
            circle = index;
            animate(ul, focus.offsetWidth * (-index));

        });
    }
    //默认当前小圆点，复制第一张图片到最后
    ol.children[0].className = 'current';
    ul.appendChild(ul.children[0].cloneNode(true));

    var num = 0;
    var circle = 0;
    var flag = true;
    arrow_r.addEventListener('click', function() {
        if (flag) {
            flag = false;
            if (num == ul.children.length - 1) {
                num = 0;
                ul.style.left = 0;
            }
            num++;
            animate(ul, focus.offsetWidth * (-num), function() {
                flag = true;
            });
            circle++;
            if (circle == ol.children.length) {
                circle = 0;
            }
            circleChange();
        }
    });

    arrow_l.addEventListener('click', function() {
        if (flag) {
            flag = false;
            if (num == 0) {
                num = ul.children.length - 1;
                ul.style.left = ul.offsetWidth * (-num);
            }
            num--;
            animate(ul, focus.offsetWidth * (-num), function() {
                flag = true;
            });
            circle--;
            if (circle < 0) {
                circle = ol.children.length - 1;
            }
            circleChange();
        }
    });

    //小圆点跟随图片，circle标志位跟随
    function circleChange() {
        for (var i = 0; i < ol.children.length; i++) {
            ol.children[i].className = '';
        }
        ol.children[circle].classList = 'current';
    }
    //常驻往右滑动
    var timer = setInterval(function() {
        arrow_r.click();
    }, 2000);


});