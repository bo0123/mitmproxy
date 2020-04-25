(function () {
    // 配置
    requirejs.config({
        // 基本路径
        baseUrl: "js/",
        // 模块标识名与模块路径映射
        paths: {
            "alerter": "./src/alerter",
            "dataService": "./src/dataService",
            'jquery': './libs/jquery-1.10.1',//注：jquery要小写

        }
    })

    // 引入使用模块
    requirejs( ['alerter'], function(alerter) {
      alerter.showMsg()
    })
})()
