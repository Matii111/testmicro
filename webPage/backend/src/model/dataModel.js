const mongoose = require('mongoose');

const dataSchema = new mongoose.Schema({
    timestamp: { type: Date, required: false },
    temperature: { type: Number, required: false },
    co2Level: { type: Number, required: false },
    light: { type: Number, required: false },
    uvLevel: { type: Number, required: false },
    humidity: { type: Number, required: false },
});

module.exports = mongoose.model('Data', dataSchema);
