// ==UserScript==
// @name         HookBase64
// @namespace    https://scrape.cuiqingcai.com
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://scrape.cuiqingcai.com/login1
// @grant        none
// ==/UserScript==

(function () {
    'use strict'

    function hook(object, attr) {
        var func = object[attr]
        object[attr] = function () {
            console.log('hooked', object, attr)
            var ret = func.apply(object, arguments)
            debugger
            return ret
        }
    }

    //hook(window, 'btoa')
    hook(JSON, 'stringify')
})()