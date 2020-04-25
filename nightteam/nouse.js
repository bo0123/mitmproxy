// ==UserScript==
// @name  HookBase64
// @namespace https://scrape.cuiqingcai.com
// /@version 0.11
// @description Hook Base64 encode function
// @author Germey
// @match https://scrape.cuiqingcai.com/login1
// @grant none
//==/UserScript=s

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

    hook(window, 'btoa')
})()
