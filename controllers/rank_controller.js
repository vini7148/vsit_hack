module.exports.region1 = function(req, res){

    var school=require("../assets/json/school1.json");

    
    return res.render("ranking.ejs", {
        title:"Ranking", 
        school:school
    })
}


module.exports.region2 = function(req, res){

    var school=require("../assets/json/school2.json");

    
    return res.render("ranking.ejs", {
        title:"Ranking", 
        school:school
    })
}



module.exports.region3 = function(req, res){

    var school=require("../assets/json/school3.json");

    
    return res.render("ranking.ejs", {
        title:"Ranking", 
        school:school
    })
}



module.exports.region4 = function(req, res){

    var school=require("../assets/json/school4.json");

    
    return res.render("ranking.ejs", {
        title:"Ranking", 
        school:school
    })
}



module.exports.region5 = function(req, res){

    var school=require("../assets/json/school5.json");

    
    return res.render("ranking.ejs", {
        title:"Ranking", 
        school:school
    })
}



module.exports.region6 = function(req, res){

    var school=require("../assets/json/school6.json");

    
    return res.render("ranking.ejs", {
        title:"Ranking", 
        school:school
    })
}



module.exports.region7 = function(req, res){

    var school=require("../assets/json/school7.json");

    
    return res.render("ranking.ejs", {
        title:"Ranking", 
        school:school
    })
}


module.exports.region = function(req, res){

    var school=require("../assets/json/school.json");

    
    return res.render("ranking_all.ejs", {
        title:"Ranking", 
        school2:school
    })
}






