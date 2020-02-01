const express= require('express');

const router = express.Router();
const homecontroller= require('../controllers/home_controller');

router.get('/',homecontroller.home );
router.use('/school', require('./school'))
router.use('/ranking', require('./ranking'))

module.exports = router;