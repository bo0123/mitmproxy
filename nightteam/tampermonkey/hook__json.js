//https://blog.csdn.net/qq_29570381/article/details/104587439
/*
* */

(function () {
    'use strict'

    var my_stringify = JSON.stringify;
    JSON.stringify = function (params) {
        console.log("yemu", params);
        //debugger
        return my_stringify(params);
    };
    JSON.stringify.toString = function () {
        console.log("low")
        return my_stringify().toString()
    }


    var my_parse = JSON.parse;
    JSON.parse = function (params) {
        console.log("yemu", params);
        debugger
        return my_parse(params);
    }

})()

