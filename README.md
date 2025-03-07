# ten_tech_test
Setup instructions

1. Clone the project
2. Checkout in branch feature-solution
3. Create, activate venv & install requirements using following command
   pip install -r requirements.txt
4. Run following command for migration
   python manage.py migrate
5. Run following command for importing csv to create sample model data
   a. For member table - python manage.py import_member_data data/initial/members.csv
   b. For inventory table - python manage.py import_inventory_data data/initial/inventory.csv
6. Run server using python manage.py runserver
7. Open url http://localhost:8000/swagger/ for swagger reference
    This has 5 API - 3 for listing of member, inventory & booking recording
    and 1 for inventory booking & other for cancel booking

8. Get ID of member & inventory from listing apis to execute following api for booking
   /api/v1/inventory/{inventory_id}/book/
9. Get booking id in response or get from bookings/v1/list api
10. Execute /api/v1/bookings/{booking_id}/cancel/ providing id of booking to cancel