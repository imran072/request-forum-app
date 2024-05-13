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

// selling.html
      // image upload
      function triggerFileInput(inputId) {
        document.getElementById(inputId).click();
    }
    
    const image1 = document.getElementById('image1');
    const image2 = document.getElementById('image2');
    const image3 = document.getElementById('image3');
    const image4 = document.getElementById('image4');
    const image5 = document.getElementById('image5');
    const preview1 = document.getElementById('preview1');
    const preview2 = document.getElementById('preview2');
    const preview3 = document.getElementById('preview3');
    const preview4 = document.getElementById('preview4');
    const preview5 = document.getElementById('preview5');
    const label1 = document.querySelector('label[for="image1"]');
    const label2 = document.querySelector('label[for="image2"]');
    const label3 = document.querySelector('label[for="image3"]');
    const label4 = document.querySelector('label[for="image4"]');
    const label5 = document.querySelector('label[for="image5"]');
    
    image1.onchange = evt => {
        const [file] = image1.files;
        if (file) {
            preview1.src = URL.createObjectURL(file);
            preview1.style.display = 'block';
            label1.style.display = 'none';
        }
    };
    
    image2.onchange = evt => {
        const [file] = image2.files;
        if (file) {
            preview2.src = URL.createObjectURL(file);
            preview2.style.display = 'block';
            label2.style.display = 'none';
        }
    };
    
    image3.onchange = evt => {
        const [file] = image3.files;
        if (file) {
            preview3.src = URL.createObjectURL(file);
            preview3.style.display = 'block';
            label3.style.display = 'none';
        }
    };
    
    image4.onchange = evt => {
        const [file] = image4.files;
        if (file) {
            preview4.src = URL.createObjectURL(file);
            preview4.style.display = 'block';
            label4.style.display = 'none';
        }
    };
    
    image5.onchange = evt => {
        const [file] = image5.files;
        if (file) {
            preview5.src = URL.createObjectURL(file);
            preview5.style.display = 'block';
            label5.style.display = 'none';
        }
    };
    
    // ad location
    const locationInput = document.getElementById('location');

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
