const mongoose = require('mongoose');

const dataSchema = new mongoose.Schema({
    content: {
        type: String,
    }
});

module.exports = mongoose.model('Data', dataSchema);
