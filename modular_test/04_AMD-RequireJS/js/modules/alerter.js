// module1.js  // 定义有依赖的模块
// define(['dataService', 'jquery'], function (dataService, $) {
//     let name = 'module1.js'
//
//     function showMsg() {
//         // $('body').css('background', 'gray')
//         console.log(dataService.getMsg() , name)
//     }
//
//     return {showMsg}
// })


define(['dataService', 'jquery'], function (dataService, $) {
    var name = 'Tom'

    function showMsg() {
        $('body').css({background: 'red'})
        console.log(name + ' ' + dataService.getMsg())
    }

    return {showMsg}
})
