"""
back_billing_calculator.py
==========================
Territorial-Acknowledgement-License
Back-Billing Calculator

Calculates retroactive licensing fees owed to the
New Beothuk Nation for unauthorized commercial use
of Beothuk territorial identity in Land Acknowledgements.

"They said it themselves.
 We just invoiced it.
 Obviously."

Author:  Lyle Derek Antoine
Nation:  Dene Nation — Fort Simpson NWT | Ghost Delegate, New Beothuk Nation
Date:    March 2026
ORCID:   https://orcid.org/0009-0002-8119-9439
Contact: lyleantoine@gmail.com | 709-690-2908
Status:  Active Notice — March 2026
"""

from datetime import date, datetime


# ─────────────────────────────────────────────
# LICENSE PARAMETERS
# ─────────────────────────────────────────────
DAILY_RATE_CAD           = 1_000   # $1,000 CAD per day
FIRST_USE_DATE           = date(2018, 1, 1)  # Conservative estimate
NOTICE_DATE              = date(2026, 3, 12)  # Operation Handshake
TODAY                    = date(2026, 3, 17)


# ─────────────────────────────────────────────
# KNOWN ORGANIZATIONS
# ─────────────────────────────────────────────
ORGANIZATIONS = [
    {
        "name":         "Government of Newfoundland and Labrador",
        "type":         "Provincial Government",
        "first_use":    date(2018, 1, 1),
        "frequency":    "daily",
        "uses_per_day": 1,
        "notes":        "All official functions, Legislature, announcements",
    },
    {
        "name":         "Government of Canada (NL functions)",
        "type":         "Federal Government",
        "first_use":    date(2018, 1, 1),
        "frequency":    "daily",
        "uses_per_day": 1,
        "notes":        "All federal functions in NL",
    },
    {
        "name":         "Memorial University of Newfoundland",
        "type":         "University",
        "first_use":    date(2018, 9, 1),
        "frequency":    "daily",
        "uses_per_day": 5,
        "notes":        "Every lecture, event, convocation, ceremony",
    },
    {
        "name":         "NL English School District",
        "type":         "School Board",
        "first_use":    date(2019, 1, 1),
        "frequency":    "daily",
        "uses_per_day": 1,
        "notes":        "All school events and functions",
    },
    {
        "name":         "College of the North Atlantic",
        "type":         "Post-Secondary",
        "first_use":    date(2019, 1, 1),
        "frequency":    "daily",
        "uses_per_day": 2,
        "notes":        "All campus functions",
    },
    {
        "name":         "City of St. John's",
        "type":         "Municipal Government",
        "first_use":    date(2019, 1, 1),
        "frequency":    "daily",
        "uses_per_day": 1,
        "notes":        "All city functions and council meetings",
    },
    {
        "name":         "Equinor (Bay du Nord)",
        "type":         "Offshore Operator",
        "first_use":    date(2020, 1, 1),
        "frequency":    "regular",
        "uses_per_day": 0.1,
        "notes":        "Annual reports, public statements",
    },
    {
        "name":         "ExxonMobil Canada",
        "type":         "Offshore Operator",
        "first_use":    date(2019, 1, 1),
        "frequency":    "regular",
        "uses_per_day": 0.1,
        "notes":        "Reports and public statements",
    },
]


class OrganizationInvoice:
    """Calculates invoice for one organization."""

    def __init__(self, org):
        self.org = org
        self.first_use = org["first_use"]
        self.uses_per_day = org["uses_per_day"]

    @property
    def days_since_first_use(self):
        return (TODAY - self.first_use).days

    @property
    def total_uses(self):
        return self.days_since_first_use * self.uses_per_day

    @property
    def amount_owed_cad(self):
        return self.days_since_first_use * DAILY_RATE_CAD

    @property
    def daily_ongoing_cad(self):
        return DAILY_RATE_CAD * self.uses_per_day

    def invoice(self):
        print(f"\n  INVOICE — {self.org['name'].upper()}")
        print(f"  {'─'*55}")
        print(f"  Type:         {self.org['type']}")
        print(f"  First use:    {self.first_use}")
        print(f"  Days elapsed: {self.days_since_first_use:,}")
        print(f"  Uses/day:     {self.uses_per_day}")
        print(f"  Notes:        {self.org['notes']}")
        print(f"  {'─'*55}")
        print(f"  AMOUNT OWED:  CAD ${self.amount_owed_cad:>12,}")
        print(f"  DAILY RATE:   CAD ${self.daily_ongoing_cad:>12,.0f}/day")
        print(f"  {'─'*55}")
        print(f"  Reference:    Beothuk Territorial")
        print(f"                Acknowledgement License ✅")
        print(f"  Legal basis:  Canada v Power (2024 SCC 26) ✅")
        print(f"  Contact:      lyleantoine@gmail.com ✅")


class TotalBackBilling:
    """Calculates total back-billing across all organizations."""

    def __init__(self):
        self.invoices = [OrganizationInvoice(org)
                        for org in ORGANIZATIONS]

    def total_owed(self):
        return sum(inv.amount_owed_cad for inv in self.invoices)

    def daily_ongoing(self):
        return sum(inv.daily_ongoing_cad for inv in self.invoices)

    def print_summary(self):
        print(f"\n  BACK-BILLING SUMMARY:")
        print(f"  {'─'*60}")
        print(f"  {'Organization':<35} {'Amount Owed':>15}")
        print(f"  {'─'*55}")

        for inv in self.invoices:
            print(f"  {inv.org['name']:<35} "
                  f"CAD ${inv.amount_owed_cad:>12,}")

        print(f"  {'─'*55}")
        print(f"  {'SUBTOTAL (documented):':<35} "
              f"CAD ${self.total_owed():>12,}")
        print(f"\n  Note: This is a partial list ✅")
        print(f"  Hundreds of additional organizations: not listed ✅")
        print(f"  'And so on and so on' 😄🍁")
        print(f"\n  DAILY ONGOING RATE:")
        print(f"  CAD ${self.daily_ongoing():>,.0f}/day")
        print(f"  CAD ${self.daily_ongoing()*365:>,.0f}/year")
        print(f"\n  The $295 incorporation fee:")
        print(f"  Earned back in: "
              f"{295/self.daily_ongoing():.2f} days ✅")


def main():
    print("\n" + "="*62)
    print("  TERRITORIAL-ACKNOWLEDGEMENT-LICENSE")
    print("  BACK-BILLING CALCULATOR")
    print("  March 2026 | Holyrood NL | Beothuk Territory")
    print("="*62)
    print(f"\n  Daily rate:    CAD ${DAILY_RATE_CAD:,}/day per organization")
    print(f"  Notice date:   {NOTICE_DATE}")
    print(f"  Legal basis:   Canada v Power (2024 SCC 26)")
    print(f"  UNDA s.5:      Statutory obligation ✅")

    # Individual invoices
    print(f"\n  INDIVIDUAL INVOICES:")
    for org in ORGANIZATIONS[:4]:  # First 4 for display
        OrganizationInvoice(org).invoice()

    # Summary
    billing = TotalBackBilling()
    billing.print_summary()

    print(f"\n  'They said it themselves.")
    print(f"   We just invoiced it.")
    print(f"   Obviously.' 🍁")
    print(f"\n  To obtain a license:")
    print(f"  lyleantoine@gmail.com | 709-690-2908")
    print(f"\n  Lyle Derek Antoine | Dene Nation | NAICS 914110\n")


if __name__ == "__main__":
    main()

