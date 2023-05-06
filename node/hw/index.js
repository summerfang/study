var express = require("express");
var app = express();

app.set("view engine", "pug");
app.set("views", "./views");

app.get("/first_template", function (req, res) {
    res.render("first_view", {title: "Express JS Tutorial", message: "Hello there!"});
});

app.get("/dynamic_view", function (req, res) {
    res.render("second", {
        name: "TutorialsPoint",
        url: "http://www.tutorialspoint.com"
    });
});

app.get("/", function (req, res) {
  res.send("Hello World!");
});

app.get("/hello", function (req, res) {
    res.send("Hello World!");
});

app.post("/hello", function (req, res) {
    res.send("You just called the post method at '/hello'!\n");
});

app.all("/test", function (req, res) {
    res.send("HTTP method doesn't have any effect on this route!");
});

app.get("/:id", function (req, res) {
    res.send("The id you specified is " + req.params.id);
});

app.get("/things/:name/:id/:row", function (req, res) {
    res.send("id: " + req.params.id + " and name: " + req.params.name + " and row: " + req.params.row);
})

app.get("/things/:id([0-9]{5})", function (req, res) { 
    res.send("id: " + req.params.id);   
});

var thing = require("./thing.js");
app.use("/thing", thing);

app.get("*", function (req, res) {
    res.send("Sorry, this is an invalid URL.");
}); // 404

app.listen(3000, function () {
  console.log("Example app listening on port 3000!");
});
