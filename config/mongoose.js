const mongoose= require('mongoose');

//setting up the connection 
mongoose.connect("mongodb://localhost/schooldb");

db = mongoose.connection;

// Shows the statement in colsole log in the form of an error
db.on('error', console.error.bind(console, "Error connecting to mongodb"));

// confirmation that the mongo database is connected
db.once('open', function(){

    console.log("connected to database :: MongoDb");
});

module.exports= db;