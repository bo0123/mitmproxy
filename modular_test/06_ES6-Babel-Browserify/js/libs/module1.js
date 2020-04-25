'use strict';

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.foo = foo;
exports.bar = bar;
// js/src/module1.js  分别暴露
function foo() {
  console.log('module1 foo()');
}
function bar() {
  console.log('module1 bar()');
}
var DATA_ARR = exports.DATA_ARR = [1, 3, 5, 1];