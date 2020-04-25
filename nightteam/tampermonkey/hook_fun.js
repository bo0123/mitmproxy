//https://www.jb51.net/article/158972.htm
/*
注意和eval不同，Function是个变长参数的构造方法，需要处理this

另外，有些网站还会用类似的机制加密页面内容，然后通过document.write输出动态解密的内容，
因此同样可以挂钩document.write，挂钩方法类似eval，这里就不重复了。
* */
//hook eval函数
(function () {
    if (window.__cr_fun) return
    window.__cr_fun = window.Function
    var myfun = function () {
        var args = Array.prototype.slice.call(arguments, 0, -1).join(","),
            src = arguments[arguments.length - 1]
        console.log("================ Function begin: args=" + args + ", length=" + src.length +
            ",caller=" + (myfun.caller && myfun.caller.name) + " ===============")
        console.log(src);
        console.log("================ Function end ================")
        return window.__cr_fun.apply(this, arguments)
    }
    myfun.toString = function () {
        return window.__cr_fun + ""
    }
    Object.defineProperty(window, 'Function', {value: myfun})
    console.log(">>>>>>>>>>>>>> Function injected: " + document.location + " <<<<<<<<<<<<<<<<<<<")
})();