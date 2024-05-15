document.addEventListener('DOMContentLoaded', function() {
    var makeSelect = document.getElementById('make');
    var modelSelect = document.getElementById('model');

    if (makeSelect && modelSelect) {
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
            'Jaguar':['i-PACE'],
            'Kia': ['Niro', 'EV6', 'EV9'],
            'Lexus': ['UX', 'RZ', 'LBX', 'NX'],
            'Maserati': ['Grecale Folgore', 'GranTurismo Folgore'],
            'Mahindra': ['XUV400EV'],
            'Mercedes-Benz': ['EQE Sedan', 'EQA', 'EQV', 'EQS SUV'],
            'MG': ['ZS', 'HS'],
            'Mitsubishi': ['Outlander', 'Eclipse Cross'],
            'Nissan': ['QASHQAI', 'X-TRAIL','LEAF'],
            'Peugeot': ['E-208', 'E-308', 'E-2008', 'E-Partner'],
            'Porsche': ['Taycan', 'Taycan 4 Cross Turismo'],
            'Opel': ['Corsa', 'Mokka'],
            'Renault': ['Megane', 'Kangoo'],
            'Suzuki': ['eVX'],
            'Tesla': ['Model S', 'Model X', 'Model 3', 'Model Y'],
            'Toyota': ['RAV4', 'Corolla', 'Camry', 'Prius','bZ4X','C-HR','Yaris','Kluger'],
            'Volvo': ['C40', 'EX30', 'EX90', 'XC40'],
            'Volkswagen': ['ID.4', 'ID.5', 'ID.Buzz']
        };

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
    }
});

// ev ads
document.addEventListener('DOMContentLoaded', function() {
    const evSlider = document.querySelector('.ev-ads-slider .slide');
    if (evSlider) {
        const ads = Array.from(evSlider.querySelectorAll('.ad'));
        const slideInterval = setInterval(shiftAd, 5000);

        function shiftAd() {
            evSlider.appendChild(ads.shift()); // moves first ad to the end
            ads.push(evSlider.lastElementChild); // updates the array
        }
    }
});

// brand logo slider
document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.brand-slider .slide');
    if (slider) {
        const logos = Array.from(slider.querySelectorAll('img'));
        const slideInterval = setInterval(shiftLogo, 3000);

        function shiftLogo() {
            slider.appendChild(logos.shift());
            logos.push(slider.lastElementChild); // updates the array
        }
    }
});

//email input validation
function validateForm() {
    let email = document.getElementById("typeEmailX-2");
    let password = document.getElementById("password_input");
    if (email && password) {
        email = email.value;
        password = password.value;
        if (/\S+@\S+\.\S+/.test(email) && /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/.test(password)) {
            alert("Thank you for signing up!");
            return true;
        } else {
            alert("Please check your inputs for proper format.");
            return false;
        }
    }
    return false;
}

// Modal script for Message Seller button
document.addEventListener('DOMContentLoaded', function() {
    if (window.jQuery) {
        $('#messageModal').on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget); // Button that triggered the modal
            var recipientUsername = button.data('recipient'); // Extract info from data-* attributes
            var recipientName = button.data('recipient-name');

            var modal = $(this);
            modal.find('#recipientUsername').val(recipientUsername);
            modal.find('#recipientName').text(recipientName);
        });
    } else {
        console.error('jQuery is not loaded');
    }
});


