const express = require('express');
const router = express.Router();
const Product = require('../models/Product');
const multer = require('multer');
const path = require('path');

// Multer setup for image uploads
const storage = multer.diskStorage({
    destination: function(req, file, cb) {
        cb(null, path.join(__dirname, '../uploads'));
    },
    filename: function(req, file, cb) {
        cb(null, Date.now() + '-' + file.originalname);
    }
});
const upload = multer({ storage });

// CRUD routes
router.get('/', async (req, res) => {
    const products = await Product.find();
    res.json(products);
});

router.post('/', upload.single('image'), async (req, res) => {
    const { name, price, description } = req.body;
    let imageUrl = '';
    if (req.file) {
        imageUrl = `/uploads/${req.file.filename}`;
    }
    const product = new Product({ name, price, description, imageUrl });
    await product.save();
    res.json(product);
});

router.put('/:id', upload.single('image'), async (req, res) => {
    const { name, price, description } = req.body;
    let update = { name, price, description };
    if (req.file) {
        update.imageUrl = `/uploads/${req.file.filename}`;
    }
    const product = await Product.findByIdAndUpdate(req.params.id, update, { new: true });
    res.json(product);
});

router.delete('/:id', async (req, res) => {
    await Product.findByIdAndDelete(req.params.id);
    res.json({ success: true });
});

module.exports = router;