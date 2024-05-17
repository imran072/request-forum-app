document.addEventListener('DOMContentLoaded', function() {
    const makeSelectIndex = document.getElementById('make-index');
    const makeSelectAdd = document.getElementById('make-add');

    if (makeSelectIndex) {
        populateMakeDropdown(makeSelectIndex, 'Any make');
        makeSelectIndex.addEventListener('change', function() {
            populateModelDropdown(this.value, 'model-index');
        });
    }

    if (makeSelectAdd) {
        populateMakeDropdown(makeSelectAdd, 'Select a brand');
        makeSelectAdd.addEventListener('change', function() {
            populateModelDropdown(this.value, 'model-add');
        });
    }
});

function populateMakeDropdown(selectElement, defaultMessage) {
    fetch('/get_brands')
        .then(response => response.json())
        .then(data => {
            selectElement.innerHTML = `<option value="any">${defaultMessage}</option>`; // Clear existing options and add default
            data.forEach(brand => {
                const option = document.createElement('option');
                option.value = brand.id;
                option.textContent = brand.name;
                selectElement.appendChild(option);
            });
        });
}

function populateModelDropdown(brandId, modelSelectId) {
    const modelSelect = document.getElementById(modelSelectId);
    fetch(`/get_models/${brandId}`)
        .then(response => response.json())
        .then(data => {
            modelSelect.innerHTML = '<option value="any">Any Model</option>'; // Clear existing options and add default
            data.forEach(model => {
                const option = document.createElement('option');
                option.value = model.id;
                option.textContent = model.name;
                modelSelect.appendChild(option);
            });
        });
}

    
    // EV ads slider
    const evSlider = document.querySelector('.ev-ads-slider .slide');
    if (evSlider) {
        const ads = Array.from(evSlider.querySelectorAll('.ad'));
        const slideInterval = setInterval(shiftAd, 5000);

        function shiftAd() {
            evSlider.appendChild(ads.shift()); // moves first ad to the end
            ads.push(evSlider.lastElementChild); // updates the array
        }
    }

    // Brand logo slider
    const slider = document.querySelector('.brand-slider .slide');
    if (slider) {
        const logos = Array.from(slider.querySelectorAll('img'));
        const slideInterval = setInterval(shiftLogo, 3000);

        function shiftLogo() {
            slider.appendChild(logos.shift());
            logos.push(slider.lastElementChild); // updates the array
        }
    }

    // Modal script for Message Seller button
    if (window.jQuery) {
        $('#messageModal').on('show.bs.modal', function(event) {
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

    // Email input validation
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

    //model dropdown
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

    // Validate image upload
    document.querySelector('form.vertical-sell-ev-form').addEventListener('submit', function(event) {
        const imageInput = document.querySelector('input[type="file"]');
        const imageError = document.getElementById('image-error');
        const validExtensions = ['image/jpeg', 'image/png', 'image/gif', 'image/jpg'];
        if (imageInput.files.length === 0) {
            imageError.style.display = 'block';
            imageError.textContent = 'Please upload an image file.';
            event.preventDefault();
            return false;
        } else if (!validExtensions.includes(imageInput.files[0].type)) {
            imageError.style.display = 'block';
            imageError.textContent = 'Please upload a valid image file (jpg, jpeg, png, gif).';
            event.preventDefault();
            return false;
        }
        imageError.style.display = 'none';
        return true;
    });


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
            headers: { 'Content-Type': 'application/json' }  
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);  // Debug to log the data to see what is actually returned
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