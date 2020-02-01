const express= require('express');
const passport = require('passport');
const router = express.Router();
const schoolcontroller= require('../controllers/school_controller');


router.get('/sign-in',schoolcontroller.sign_in);

router.get('/sign-up', schoolcontroller.sign_up);

router.post('/create',schoolcontroller.create);

router.post('/create-session',passport.authenticate('local', {failureRedirect:"/"}),schoolcontroller.create_session);

router.get('/destroy-session', schoolcontroller.destroy_session);

router.get('/profile/:id',passport.checkAuthentication, schoolcontroller.profile);

router.post('/update/:id', passport.checkAuthentication, schoolcontroller.update);

router.get('/registered', schoolcontroller.registered_schools);
module.exports = router;