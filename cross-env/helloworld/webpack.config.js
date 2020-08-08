const path = require("path");

module.exports = {
    "entry" : "./src/main/index.js",
    output: {
        path: path.resolve(__dirname, 'build'),
        filename: "bundle.js"

    }
}


