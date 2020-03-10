function print(name) {
    console.log(name);
}

var names = ["Jack", "Jecci", "Ram", "Tom"];

for (let i=0, totalNames = names.length; i < totalNames; i = i +1 ) {
    print(names[i])
}

var names = ["Jack", "Jecci", "Ram", "Tom"];

names.forEach(name=>print(name));

