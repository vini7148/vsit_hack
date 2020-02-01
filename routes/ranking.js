const express= require('express');

const router = express.Router();
const rankcontroller= require('../controllers/rank_controller')

router.get('/north_west',rankcontroller.region1);
router.get('/central', rankcontroller.region2);
router.get('/north',rankcontroller.region3);
router.get('/west',rankcontroller.region4);
router.get('/south',rankcontroller.region5);
router.get('/east',rankcontroller.region6);
router.get('/north_east',rankcontroller.region7);
router.get('/',rankcontroller.region);



module.exports = router;