document.addEventListener('DOMContentLoaded', function() {
    var makeSelect = document.getElementById('make');
    var modelSelect = document.getElementById('model');
    var yearSelect = document.getElementById('year');
    var mileageSelect = document.getElementById('mileage');
    var topSpeedSelect = document.getElementById('top_speed');
    var accelerationSelect = document.getElementById('acceleration');
    var priceSelect = document.getElementById('price');
    var colorSelect = document.getElementById('color');

    // Car Models Data
    var carModels = {
        'Audi': ['Q4 e-tron', 'SQ8 e-tron', 'Q8 e-tron', 'e-tron GT'],
        'Bentley': ['Bentayga', 'Bentayga A', 'Bentayga Azure', 'Bentayga S'],
        'BMW': ['iX', 'iX4', 'iX5', 'iX7'],
        'BYD': ['Dolphin', 'Seal', 'Atto 3'],
        'Chery': ['Omoda E5'],
        'Chevrolet': ['Equinox EV', 'Silverado EV', 'Blazer EV'],
        'Fiat': ['500e'],
        'Fisker': ['Ocean', 'PEAR', 'Alaska', 'Ronin'],
        'Ford': ['Mustang Mach-E', 'Escape PHEV', 'Ranger PHEV', 'E-Transit'],
        'Honda': ['Prologue'],
        'Hyundai': ['Ioniq 5', 'Ioniq 6', 'Kona EV', 'Ioniq 7'],
        'JAC Motors': ['e-J7', 'e-JS4', 'e-JS1'],
        'Jaguar': ['i-PACE'],
        'Kia': ['Niro', 'EV6', 'EV9'],
        'Lexus': ['UX', 'RZ', 'LBX', 'NX'],
        'Maserati': ['Grecale Folgore', 'GranTurismo Folgore'],
        'Mahindra': ['XUV400EV'],
        'Mercedes-Benz': ['EQE Sedan', 'EQA', 'EQV', 'EQS SUV'],
        'MG': ['ZS', 'HS'],
        'Mitsubishi': ['Outlander', 'Eclipse Cross'],
        'Nissan': ['QASHQAI', 'X-TRAIL', 'LEAF'],
        'Peugeot': ['E-208', 'E-308', 'E-2008', 'E-Partner'],
        'Porsche': ['Taycan', 'Taycan 4 Cross Turismo'],
        'Opel': ['Corsa', 'Mokka'],
        'Renault': ['Megane', 'Kangoo'],
        'Suzuki': ['eVX'],
        'Tesla': ['Model S', 'Model X', 'Model 3', 'Model Y'],
        'Toyota': ['RAV4', 'Corolla', 'Camry', 'Prius', 'bZ4X', 'C-HR', 'Yaris', 'Kluger'],
        'Volvo': ['C40', 'EX30', 'EX90', 'XC40'],
        'Volkswagen': ['ID.4', 'ID.5', 'ID.Buzz']
    };

    // Populate Model Dropdown
    makeSelect.onchange = function() {
        modelSelect.length = 1; // Reset to default option

        var selectedMake = makeSelect.value;

        if (selectedMake in carModels) {
            carModels[selectedMake].forEach(function(model) {
                var option = new Option(model, model);
                modelSelect.add(option);
            });
        }
    };

    // Example of populating other dropdowns (e.g., years)
    var years = [2018, 2019, 2020, 2021, 2022, 2023];
    years.forEach(function(year) {
        var option = new Option(year, year);
        yearSelect.add(option);
    });

    var mileageOptions = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000];
    mileageOptions.forEach(function(mile) {
        var option = new Option(mile + " km", mile);
        mileageSelect.add(option);
    });

    var topSpeedOptions = [120, 130, 140, 150, 160, 170, 180, 200];
    topSpeedOptions.forEach(function(speed) {
        var option = new Option(speed + " km/h", speed);
        topSpeedSelect.add(option);
    });

    var accelerationOptions = [6, 5.5, 5, 4.5, 4, 3.5, 3];
    accelerationOptions.forEach(function(acc) {
        var option = new Option("0-100 km/h in " + acc + " seconds", acc);
        accelerationSelect.add(option);
    });

    var priceOptions = [20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000];
    priceOptions.forEach(function(price) {
        var option = new Option("$" + price, price);
        priceSelect.add(option);
    });

    var colorOptions = ['Black', 'White', 'Red', 'Blue', 'Silver', 'Grey'];
    colorOptions.forEach(function(color) {
        var option = new Option(color, color);
        colorSelect.add(option);
    });
});
