from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    makes = ['Audi', 'Bentley', 'BMW', 'BYD', 'Chery', 'Chevrolet', 'Fiat', 'Fisker', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Kia', 'Lexus', 'Maserati', 'Mahindra', 'Mercedes-Benz', 'MG', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Opel', 'Renault', 'Suzuki', 'Tesla', 'Toyota', 'Volvo', 'Volkswagen']
    distances = [5, 10, 15, 20, 30, 40, 50, 75, 100, 150, 200]
    prices = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    ads = [
        {'name': 'Tesla Model 3', 'price': 25000, 'description': 'Model 3 is designed for electric-powered performance, with quick acceleration, long range and fast charging.', 'image': 'Tesla_Model_3.png', 'alt': 'Tesla_Model_3'},
        {'name': 'Toyota Camry', 'price': 20000, 'description': 'Toyota Electrified - Towards the future', 'image': 'Toyota_Camry.png', 'alt': 'Toyota_Camry'},
        {'name': 'Tesla Model S', 'price': 28000, 'description': 'Model 3 is designed for electric-powered performance, with quick acceleration, long range and fast charging.', 'image': 'Tesla_Model_X.png', 'alt': 'Tesla_Model_S'}
    ]
    brand_logos = ['Tesla.png', 'Honda.png', 'Fisker.png', 'Ford.png', 'Audi.png', 'Renault.png', 'Toyota.png', 'Volvo.png', 'Maserati.png', 'Nissan.png', 'Mahindra.png', 'Kia.png', 'Jaguar.png', 'Hyundai.png', 'BYD.png', 'Volkswagen.png', 'Bentley.png', 'BMW.png']

    return render_template('index.html', makes=makes, distances=distances, prices=prices, ads=ads, brand_logos=brand_logos)

@app.route('/vehicles')
def vehicles():
    makes = ['Audi', 'Bentley', 'BMW', 'BYD', 'Chery', 'Chevrolet', 'Fiat', 'Fisker', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Kia', 'Lexus', 'Maserati', 'Mahindra', 'Mercedes-Benz', 'MG', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Opel', 'Renault', 'Suzuki', 'Tesla', 'Toyota', 'Volvo', 'Volkswagen']
    years = list(range(2000, 2024))
    mileage = ['5000', '10000', '15000', '20000', '25000', '30000', '35000', '40000', '45000', '50000']
    top_speed = ['120', '150', '180', '200', '220', '240', '260']
    acceleration = ['3', '4', '5', '6', '7', '8', '9', '10']
    prices = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Silver', 'Gray', 'Yellow']

    return render_template('search.html', makes=makes, years=years, mileage=mileage, top_speed=top_speed, acceleration=acceleration, prices=prices, colors=colors)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)
