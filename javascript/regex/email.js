function isEmailValid(email) {
	var re = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/g;
	var result = email.match(re);
	return (isNaN(result));
}

module.exports = isEmailValid;