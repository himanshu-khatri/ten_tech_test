# ten_tech_test
# DB used -> SQLite, framework used - Django
Setup instructions

1. Clone the project
2. Checkout in branch feature-solution
3. Create, activate venv & install requirements using following command. <br/>
   pip install -r requirements.txt
4. Run following command for migration. <br/>
   python manage.py migrate
5. Run following command for importing csv to create sample model data. <br/>
    For member table - python manage.py import_member_data data/initial/members.csv <br/>
    For inventory table - python manage.py import_inventory_data data/initial/inventory.csv. <br/>
6. Run server using python manage.py runserver
7. Open url http://localhost:8000/swagger/ for swagger reference. <br/>
    This has 5 API - 3 for listing of member, inventory & booking recording
    and 1 for inventory booking & other for cancel booking

8. Get ID of member & inventory from listing apis to execute following api for booking. <br/>
   /api/v1/inventory/{inventory_id}/book/
9. Get booking id in response or get from bookings/v1/list api
10. Execute /api/v1/bookings/{booking_id}/cancel/ providing id of booking to cancel