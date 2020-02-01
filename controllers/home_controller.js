module.exports.home = function(req, res){

    var school = require('../assets/json/school.json')
    
    return res.render('home', {
        title:"BriteStorm",
        school2:school
    })
}