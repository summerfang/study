const isEmailValid = require("../email.js");

QUnit.module('isEmailValid');

QUnit.test('test whether email address is valid', assert => {
let testEmails = [
					['summerfang@gmail.com', 1],
					['summer.fang@gmail.com', 1],
					['123@gmail.com', 1],
					['123@gmail.', 0],
					['123@gmail', 0]
				 ];

testEmails.forEach(function(item, index, array){
  assert.equal(isEmailValid(item[0]), item[1], item[0] + "is " + (item[1] == 1));

});
});