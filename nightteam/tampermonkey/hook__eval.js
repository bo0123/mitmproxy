//https://www.jb51.net/article/158972.htm
/*
现在很多网站都上了各种前端反爬手段，无论手段如何，最重要的是要把包含反爬手段的前端javascript代码加密
隐藏起来，然后在运行时实时解密动态执行。

动态执行js代码无非两种方法，即eval和Function。那么，不管网站加密代码写的多牛，我们只要将这两个方法
hook住，即可获取到解密后的可执行js代码。

注意，有些网站会检测eval和Function这两个方法是否原生，因此需要一些小花招来忽悠过去。
* */
//hook eval函数
//这段代码执行后，之后所有的eval操作都会在控制台打印输出将要执行的js源码。
// eval+""   "function eval() { [native code] }"

(function () {
    if (window.__cr_eval) return
    window.__cr_eval = window.eval
    var myeval = function (src) {
        console.log("================ eval begin: length=" + src.length + ",caller=" + (myeval.caller && myeval.caller.name) + " ===============")
        console.log(src);
        console.log("================ eval end ================")
        return window.__cr_eval(src)
    }
    var _myeval = myeval.bind(null)
    _myeval.toString = window.__cr_eval.toString
    Object.defineProperty(window, 'eval', {value: _myeval})
    console.log(">>>>>>>>>>>>>> eval injected: " + document.location + " <<<<<<<<<<<<<<<<<<<")
})();

//Nightteam  妄为
window.__cr_eval = window.eval
var myeval = function (src) {
    console.log("================ eval begin: length=" + src.length + ",caller=" + (myeval.caller && myeval.caller.name) + " ===============")
    console.log(src);
    console.log("================ eval end ================")
    return window.__cr_eval(src)
}
//这样重写后不是原生的方法了,把toString方法也重写一下
myeval.toString = function () {
    return "function eval() { [native code] }"
}
Object.defineProperty(window, 'eval', {value: myeval})


