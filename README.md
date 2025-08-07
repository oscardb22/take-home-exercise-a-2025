# Parking Garage Reservation & Payment API

This take-home exercise involves building a backend service for a Parking Garage Reservation & Payment API. Candidates may use either Ruby (Rails) or Python (Django), and should set up any necessary scaffolding based on this prompt. The solution must be implemented in the provided repository, including API endpoints, data models, and business logic as described below.

## Features

1. **Garages & Map**
   - Store 5 garages
   - Expose an endpoint to list all garages.

2. **Availability**
   - Given a garage ID, a start time, and an end time, return all free spots in that interval.

3. **Reservation**
   - Create a reservation: user selects a spot, start/end times.
   - Prevent double-booking.
   - Customers should be able to hold a spot for 10 minutes before they need to confirm their reservation.
   - If the customer does not confirm the reservation within 10 minutes, the spot should be released.

4. **Payment**
   Don't worry about payments implementation, assume it is already done through the following classes:
   ```ruby
   class PaymentService
       def make_payment(amount, customer_id)
           # returns a Stripe transaction ID or nil if the payment fails
       end
   end
   ```
   ```python
   class PaymentService:
       def make_payment(self, amount, customer_id):
           # returns a Stripe transaction ID or None if the payment fails
           pass
   ```

5. **User Reservations**
   - Allow a customer to list their upcoming and past reservations.


## Deliverables

- **database schema** or migrations to establish necessary entities/relationships.
- **API endpoints** for the above use cases, backed by appropriate business logic.
- Automated tests.
- A few **curl** or **HTTPie** examples demonstrating each endpoint.
- A **README** explaining your setup and design choices, and with instructions on the steps to run the project.


http://localhost:8000/api/schema/redoc/

http://localhost:8000/api/schema/swagger-ui/
