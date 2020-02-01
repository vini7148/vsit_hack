const passport= require("passport");
const LocalStrategy= require('passport-local').Strategy;
const School= require('../models/school');

passport.use(new LocalStrategy({

    usernameField:'email'
},
    function(email,password,done){
        School.findOne({email:email},function(err,user){
            // if there was an internal error in accessing the database
            if(err){
                console.log("there was an error accessing the school database");
                return done(err);
            }
            //invalid username/password
            else if(!user ||( user.password != password)){
                return done(null, false);
            }
            //school is present 
            else {
                return done (null, user);
            }


        })

}));


// if the sign in is authenticated this will save the user's id as a cookie using express-session so user can
// accessed later on 
passport.serializeUser( function(school, done){
    return done(null, school.id);
});


// to find the user once the user is signed in 
passport.deserializeUser(function(id, done){

    School.findById(id, function(err, school){

        if(err){
            console.log("Error in deserializing in passport");
            return done(err);
        }
        return done(null, school);
    })
});


// check if the user is signed in 
passport.checkAuthentication = function(req, res, next){
    if(req.isAuthenticated()){
        return next();
    }
    return res.redirect('/school/sign-in');
}

// sent the user to locals for views if the user is signed in 

passport.setAuthenticatedUser = function(req,res,next){
    if(req.isAuthenticated()){
        res.locals.school= req.user;
    }
    return next();
}

module.exports = passport;