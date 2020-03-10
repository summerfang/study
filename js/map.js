var names = ["Jack",  "Jecci",  "Ram", "Tom"];

var upperCaseNames = [];

for (let i=0, totalNames = names.length; i < totalNames; i= i+1) {
    upperCaseNames[i] = names[i].toUpperCase();
}


var names = ["Jack", "Jecci", "Ram", "Tom"];

var upperCaseNames = names.map(name => name.toUpperCase())