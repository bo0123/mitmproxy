//hook window对象的__pt__属性的设置与取值
(function(){
    'use strict';
    var pre = window._pt_;
    Object.defineProperty(window,"_pt_", {
        get:function(){
            console.log("pre:", pre)
        },
        set:function(val){
            console.log("_pt_:", val);
            debugger;
            pre = val;
            return pre;
        }
    })
})();