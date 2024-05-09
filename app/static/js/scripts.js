document.addEventListener('DOMContentLoaded', function() {
    var makeSelect = document.getElementById('make');
    var modelSelect = document.getElementById('model');

    var carModels = {
        'Audi': ['Q4 e-tron', 'SQ8 e-tron', 'Q8 e-tron', 'e-tron GT'],
        'Bentley': ['Bentayga', 'Bentayga A', 'Bentayga Azure', 'Bentayga S'],
        'BMW': ['iX', 'iX4', 'iX5', 'iX7'],
        'BYD': ['Dolphin', 'Seal', 'Atto 3'],
        'Chery': ['Omoda E5'],
        'Chevrolet': ['Equinox EV', 'Silverado EV', 'Blazer EV'],
        'Fiat': ['500e'],
        'Fisker': ['Ocean', 'Pear', 'Alaska', 'Ronin'],
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
        'Nissan': ['Qashqai', 'X-Trail', 'Leaf'],
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

    function populateMakesDropdown(selectedMake) {
        makeSelect.innerHTML = '<option value="any">Any Make</option>';

        var carMakes = Object.keys(carModels);
        carMakes.forEach(make => {
            var option = new Option(make, make);
            if (make === selectedMake) {
                option.selected = true;
            }
            makeSelect.add(option);
        });
    }

    makeSelect.onchange = function() {
        modelSelect.length = 1; // goes back to default option

        var selectedMake = makeSelect.value;

        if (selectedMake in carModels) {
            carModels[selectedMake].forEach(function(model) {
                var option = new Option(model, model);
                modelSelect.add(option);
            });
        }
    };

    function initializeModels() {
        var selectedMake = makeSelect.value;
        var selectedModel = modelSelect.getAttribute('data-selected');

        if (selectedMake in carModels) {
            carModels[selectedMake].forEach(function(model) {
                var option = new Option(model, model);
                modelSelect.add(option);

                if (model === selectedModel) {
                    option.selected = true;
                }
            });
        }
    }

    populateMakesDropdown(new URLSearchParams(window.location.search).get('make'));
    initializeModels(); // initialises models on page load

    // ev ads slider
    const evSlider = document.querySelector('.ev-ads-slider .slide');
    const ads = Array.from(evSlider.querySelectorAll('.ad'));

    function shiftAd() {
        const firstAd = ads.shift();
        evSlider.appendChild(firstAd);
        ads.push(evSlider.lastElementChild);
    }

    setInterval(shiftAd, 5000);

    // brand logo slider
    const brandSlider = document.querySelector('.brand-slider .slide');
    const logos = Array.from(brandSlider.querySelectorAll('img'));

    function shiftLogo() {
        const firstLogo = logos.shift();
        brandSlider.appendChild(firstLogo);
        logos.push(brandSlider.lastElementChild);
    }

    setInterval(shiftLogo, 3000);

   
});

 // clear individual filters
 window.clearFilter = function(filterName) {
    var filterElement = document.querySelector(`[name="${filterName}"]`);
    if (filterElement) {
        if (filterElement.tagName === 'SELECT') {
            filterElement.value = 'any';
        } else {
            filterElement.value = '';
        }
    }
    document.getElementById('filter-form').submit();
}

// clear all filters
window.clearAllFilters = function() {
    var formElements = document.getElementById('filter-form').elements;
    for (var i = 0; i < formElements.length; i++) {
        var element = formElements[i];
        if (element.tagName === 'SELECT') {
            element.value = 'any';
        } else {
            element.value = '';
        }
    }
    document.getElementById('filter-form').submit();
}

// listeners for x buttons and clear all button
document.querySelectorAll('.filter-button').forEach(button => {
    button.onclick = function() {
        var filterName = this.getAttribute('data-filter');
        clearFilter(filterName);
    };
});

document.getElementById('clear-all').onclick = function() {
    clearAllFilters();
};