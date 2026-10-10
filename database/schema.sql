CREATE TABLE cars (
    car_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    company VARCHAR(50) NOT NULL,
    type VARCHAR(20) NOT NULL,
    manufacturing_year INTEGER NOT NULL,
    horsepower INTEGER NOT NULL
);

INSERT INTO cars (car_id, name, company, type, manufacturing_year, horsepower)
VALUES
    (1, 'Nissan GT-R R35', 'Nissan', 'JDM', 2007, 473),
    (2, 'Honda NSX', 'Honda', 'JDM', 1990, 270),
    (3, 'Toyota Supra A80 Turbo', 'Toyota', 'JDM', 1993, 320),
    (4, 'Bugatti Chiron Super Sport 300+', 'Bugatti', 'Hypercar', 2021, 1578),
    (5, 'Koenigsegg Jesko Absolut', 'Koenigsegg', 'Hypercar', 2024, 1280),
    (6, 'Koenigsegg Regera', 'Koenigsegg', 'Hypercar', 2016, 1500),
    (7, 'Dodge Challenger Scat Pack', 'Dodge', 'Muscle', 2015, 485),
    (8, 'Chevrolet Camaro SS', 'Chevrolet', 'Muscle', 2016, 455),
    (9, 'Chevrolet Corvette C6 ZR1', 'Chevrolet', 'Muscle', 2009, 638),
    (10, 'Dodge Viper V10', 'Dodge', 'Muscle', 1992, 400),
    (11, 'Ferrari 488 GTB', 'Ferrari', 'Italian', 2015, 660),
    (12, 'Lamborghini Huracan EVO', 'Lamborghini', 'Italian', 2019, 631),
    (13, 'Lamborghini Aventador SVJ', 'Lamborghini', 'Italian', 2018, 759);