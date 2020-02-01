const School = require('../models/school');

// rendering the sign-up page
module.exports.sign_up= function(req,res){
    return res.render('sign-up',{
        title:"school sign-up"
    } );
}

// rendering the sign-in page
module.exports.sign_in = function(req, res){
    return res.render('sign-in', {
        title:"school sign-in"
    })
}

// adding a new school to the database
module.exports.create= function(req, res){

    if(req.body.password != req.body.confirm_password){
        console.log("the password and the confirm-password are not matching");
        return res.redirect("/school/sign-up");
    }

    School.findOne({email:req.body.email}, function(err, schl){

        if(err){
            console.log("there was a error in finding the worker in database during create session");
            return res.redirect('back');
        }
        if(!schl){
            School.create(req.body, function(err, wrkr){
                if(err){
                    console.log("there was an error in registering the user");
                    res.redirect('back');
                }
                else {
                    console.log("The user has been created and added in the database");
                    return res.redirect('/school/sign-in');

                }


            })
        
            
        }
        else{
            console.log("A user with this email already exists");
            return res.redirect('/school/sign-up');
        }
    })

}

module.exports.create_session = function(req, res){
    console.log("succesfully signed in ");
    return res.redirect("/");

}

module.exports.destroy_session = function(req,res){
    req.logout();
    return res.redirect('/');

}


// render the user profile page 
module.exports.profile = function (req, res) {

    School.findById(req.params.id, function (err, school) {
        return res.render('school_details',
            {
                title: 'school-details',
                profile_school:school
            });

    })

   
};


module.exports.update = async function (req, res) {

    if (req.params.id == req.user.id) {
        try {
            
            School.findByIdAndUpdate(req.params.id,req.body , function (err, user) {
                
                res.redirect('back');


            })
            
            
            
        }
        catch(err){
           // req.flash('error', err);
            console.log(err);
            return res.redirect('back');
        }

    }
    else {
        
       // req.flash('error', 'Unauthorized !')
        res.status(401).send('Unauthorized');
    }
}

module.exports.registered_schools = async function(req,res){

    let schools = await School.find({},);
    
    return res.render('registered_list', {
        title:"registered school list",
        schools:schools
    })


};