const isEmailValid = require("../email.js");

let testEmails = [
	['summerfang@gmail.com', 1],
	['summer.fang@gmail.com', 1],
	['123@gmail.com', 1],
	['123@gmail.', 0],
	['123@gmail', 0]
];

QUnit.module('isEmailValid');

testEmails.forEach(function (item, index, array) {
	QUnit.test('test whether email address is valid', assert => {
		assert.equal(isEmailValid(item[0]), item[1], item[0] + "is " + (item[1] == 1));
	});
});
