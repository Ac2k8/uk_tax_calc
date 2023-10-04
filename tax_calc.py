

class TaxCalc:

    def __init__(self, annual):

        self.annual_pay = annual
        self.taxable = self.annual_pay

        self.tax_paid = 0
        self.additional_thresh = 125140
        self.higher_thresh = 50271
        self.basic_thresh = 12570

        self.additional_rate = 0.45
        self.higher_rate = 0.40
        self.basic_rate = 0.2

# ------------------------------------------------------------------------------
    def calculate(self):

        # tax everything > additional threshold
        if self.taxable > self.additional_thresh:
            self.tax_paid += (self.taxable - self.additional_thresh) * self.additional_rate
            self.taxable = self.additional_thresh

        # additional thresh > tax everything > higher threshold
        if self.taxable > self.higher_thresh:
            self.tax_paid += (self.taxable - self.higher_thresh) * self.higher_rate
            self.taxable = self.higher_thresh

        # higher thresh > tax everything > basic thresh
        if self.taxable > self.basic_thresh:
            self.tax_paid += (self.taxable - self.basic_thresh) * self.basic_rate
            self.taxable = 0

        annual_pay_after_tax = self.annual_pay - self.tax_paid

        return annual_pay_after_tax, self.tax_paid




