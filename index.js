const express = require("express");// include express to set up the server
const port = 7000;
const app= express();
const expressLayouts= require("express-ejs-layouts");
const db= require("./config/mongoose");
const session = require("express-session");// used for session cookies
const passport= require("passport");
const passportLocal= require("./config/passport-local-strategy");
const MongoStore = require("connect-mongo")(session);// stores the cookie used to sign in in mongo database

//helps in decoding and reading the form data 
app.use(express.urlencoded())

//static files
app.use(express.static("./assets"));

// using layouts in the javascript backend
// keeping layouts before the routes to ensure smooth working 
app.use(expressLayouts);

//extracting the css and javascript files for the individual pages and 
//including it on the layouts at the right place
app.set("layout extractStyles", true);
app.set("layout extractScripts", true);




//set up the view engine
app.set('view engine','ejs');
app.set('views', './views');

// set up the session cookies to store the user's id in encrypted form
// should be after setting the views

app.use(session({
    name:"foocheck",// name of the cookie
    secret:"foocheck",// code used to encrpyt the user-id
    saveUninitialized:false,
    resave:false,
    cookie:{
        maxAge:1000*60*120// time for which the cookie will remain alive
    }, 
    store:new MongoStore({
        autoRemove:'disabled',
        mongooseConnection:db
    }, function(err){
        console.log(err||"connect-mongo is working");
    })

    
}));

//should be after session set up

app.use(passport.initialize());
app.use(passport.session());

app.use(passport.setAuthenticatedUser);


//set up routers 
// routers should be mentioned in the end 
app.use('/', require('./routes'));


app.listen(port, function(err){
    if(err){
        console.log("The server is not able to run due to the error", err);
    }
    else{
        console.log(`the server is up and running on port ${port}`);
    }
})
