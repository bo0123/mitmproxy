(function () {
    require.config({
        //基本路径
        baseUrl: "js/",
        //模块标识名与模块路径映射
        paths: {
            //第三方库
            'jquery': './libs/jquery-1.10.1',
            'angular': './libs/angular',
            //自定义模块
            "alerter": "./modules/alerter",
            "dataService": "./modules/dataService"
        },
        /*
         配置不兼容AMD的模块
         exports : 指定与相对应的模块名对应的模块对象
         */
        shim: {
            'angular': {
                exports: 'angular'
            }
        }
    })
    //引入使用模块
    require(['alerter', 'angular'], function (alerter, angular) {
        alerter.showMsg()
        console.log(angular);
    })
})()
