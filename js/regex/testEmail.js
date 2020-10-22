var isEmailValid = require("./email.js");

let testEmails = ['summerfang@gmail.com',
				  'summer.fang@gmail.com',
				  '909560719@qq.com', 
				  'asdf asdf@ee.com', 
				  'test@ad',
				  'Abc@aa.dd'];

testEmails.forEach(function(item, index, array){
	if(isEmailValid(item)) {
		console.log(item, "is a valid email address");
	} else {
		console.log(item, "is not a valid email address");
	}
});