from datetime import datetime
from dateutil.relativedelta import relativedelta


class Client:
    def __init__(self, id:int = 0, person_id: int = 0, membership_type = "regular", payment_pending=True,
                 last_payment=None,next_payment=None):
        self._id = id
        self._person_id = person_id
        self._membership_type = membership_type
        self._payment_pending = payment_pending
        self._last_payment = self.calculate_date() if type(last_payment) == type(None) else last_payment
        self._next_payment = self.calculate_next_date() if type(next_payment) == type(None) else next_payment

    @property
    def id(self):
        return self._id

    @property
    def person_id(self):
        return self._person_id

    @property
    def membership_type(self):
        return self._membership_type

    @property
    def payment_pending(self):
        return self._payment_pending

    @property
    def last_payment(self):
        return self._last_payment

    @property
    def next_payment(self):
        return self._next_payment

    @id.setter
    def id(self, id):
        self._id = id

    @person_id.setter
    def person_id(self, person_id):
        self._person_id = person_id

    @membership_type.setter
    def membership_type(self, value):
        self._membership_type = value

    @payment_pending.setter
    def payment_pending(self, value):
        self._payment_pending = value

    @last_payment.setter
    def last_payment(self, value):
        self._last_payment = value

    @next_payment.setter
    def next_payment(self, value):
        self._next_payment = value

    def calculate_date(self):
        return datetime.now().date()

    def calculate_next_date(self):
        today = self.calculate_date()
        next_date = today + relativedelta(months=1)
        return next_date


    def __str__(self):
        return f"ClientID{self.person_id},Membership:{self._membership_type},PaymentPending:{self._payment_pending},LastPayment:{self._last_payment},NextPayment:{self._next_payment}"

