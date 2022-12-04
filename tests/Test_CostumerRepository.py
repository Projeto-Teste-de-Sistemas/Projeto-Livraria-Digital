from repositories.customer_repository import CustomerRepository
from entities.customer import Customer
 
def test_check_if_customer_exists():
    # Arrange
    customer_repository = CustomerRepository()
    customer_repository.list_customers = []
    customer1 = Customer(1, "Kauã")
    customer2 = Customer(2, "Paulo")
    # Act
 
    customer_repository.add_customer(customer1)
    resultOK = customer_repository.verify_exists_customer(customer1)
    resultNOK = customer_repository.verify_exists_customer(customer2)
 
    # Assert
    assert resultOK == True
    assert resultNOK == False
 
def test_add_costumer():
    # Arrange
    customer_repository = CustomerRepository()
    customer_repository.list_customers = []
    customer1 = Customer(1, "Kauã")
    customer2 = Customer(2, "Paulo")
    customer3 = Customer(3, "José")
 
    # Act
    customer_repository.add_customer(customer1)
    customer_repository.add_customer(customer2)
 
    # Assert
    assert len(customer_repository.list_customers) == 2
    assert not customer3 in customer_repository.list_customers
 
def test_get_client():
    # Arrange
    customer_repository = CustomerRepository()
    customer_repository.list_customers = []
    customer1 = Customer(1, "Meire")
 
    # Act
    customer_repository.add_customer(customer1)
    resultOK = customer_repository.get_customer(1)
 
    # Assert
    assert resultOK == True
   
 
 
 
 
 
 
 
 
 
 

