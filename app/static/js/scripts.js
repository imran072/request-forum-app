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
});

// ev ads
document.addEventListener('DOMContentLoaded', function() {
    const evSlider = document.querySelector('.ev-ads-slider .slide');
    const ads = Array.from(evSlider.querySelectorAll('.ad'));
    const slideInterval = setInterval(shiftAd, 5000);

    function shiftAd() {
        evSlider.appendChild(ads.shift()); // moves first ad to the end
        ads.push(evSlider.lastElementChild); // updates the array
    }
});

// brand logo slider
document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.brand-slider .slide');
    const logos = Array.from(slider.querySelectorAll('img'));
    const slideInterval = setInterval(shiftLogo, 3000);

    function shiftLogo() {
        slider.appendChild(logos.shift());
        logos.push(slider.lastElementChild); // updates the array
    }
});

//email input validation
function validateForm() {
    let email = document.getElementById("typeEmailX-2").value;
    let password = document.getElementById("password_input").value;
    if (/\S+@\S+\.\S+/.test(email) && /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/.test(password)) {
        alert("Thank you for signing up!");
        return true;
    } else {
        alert("Please check your inputs for proper format.");
        return false;
    }
}

document.getElementById('make').addEventListener('change', function() {
    const brandId = this.value;
    fetch(`/get_models/${brandId}`)
      .then(response => response.json())
      .then(data => {
        const modelSelect = document.getElementById('model');
        modelSelect.innerHTML = ''; // Clear existing options
        data.forEach(model => {
          const option = document.createElement('option');
          option.value = model.id;
          option.textContent = model.name;
          modelSelect.appendChild(option);
        });
    });
});

function validateImage() {
    const imageInput = document.querySelector('input[type="file"]');
    const imageError = document.getElementById('image-error');
    const validExtensions = ['image/jpeg', 'image/png', 'image/gif', 'image/jpg'];
    if (imageInput.files.length === 0) {
      imageError.style.display = 'block';
      imageError.textContent = 'Please upload an image file.';
      return false;
    } else if (!validExtensions.includes(imageInput.files[0].type)) {
      imageError.style.display = 'block';
      imageError.textContent = 'Please upload a valid image file (jpg, jpeg, png, gif).';
      return false;
    }
    imageError.style.display = 'none';
    return true;
}

function confirmDelete2(vehicleId) {
    if(confirm('Are you sure you want to delete this listing?')) {
        fetch('/delete_listing/' + vehicleId, { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                if(data.success) {
                    window.location.reload();  // Reload the page to update the list
                } else {
                    alert('Error deleting listing.');
                }
            });
    }
}
function confirmDelete(vehicleId) {
    if(confirm('Are you sure you want to delete this listing?')) {
        fetch('/delete_listing/' + vehicleId, { 
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }  // Ensure your server expects JSON if needed
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);  // Debug: log the data to see what is actually returned
            if(data.success) {
                window.location.reload();  // Reload the page to update the list
            } else {
                alert('Error deleting listing.');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert('Failed to delete the listing due to a network error.');
        });
    }
}

