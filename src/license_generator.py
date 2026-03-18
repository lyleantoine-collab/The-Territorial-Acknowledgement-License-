"""
license_generator.py
====================
Territorial-Acknowledgement-License
License Agreement Generator

Generates formal license agreements for organizations
wishing to legitimately use Beothuk territorial identity
in Land Acknowledgements.

"The acknowledgement belongs to the Nation.
 The license belongs to the Nation.
 The revenue belongs to the Nation.
 Obviously."

Author:  Lyle Derek Antoine
Nation:  Dene Nation — Fort Simpson NWT | Ghost Delegate, New Beothuk Nation
Date:    March 2026
ORCID:   https://orcid.org/0009-0002-8119-9439
Contact: lyleantoine@gmail.com | 709-690-2908
Status:  Active Notice — March 2026
"""

from datetime import date, timedelta


DAILY_RATE_CAD    = 1_000
ANNUAL_RATE_CAD   = 300_000    # Annual license (discount)
VOLUME_RATE_CAD   = 200_000    # Volume discount (5+ sites)
TODAY             = date(2026, 3, 17)


class LicenseGenerator:
    """Generates Land Acknowledgement license agreements."""

    def __init__(self, org_name, org_type,
                 license_type="annual",
                 retroactive_days=0,
                 payment_method="CAD"):
        self.org = org_name
        self.type = org_type
        self.license = license_type
        self.retro_days = retroactive_days
        self.payment = payment_method

    @property
    def license_fee(self):
        if self.license == "daily":
            return DAILY_RATE_CAD
        elif self.license == "annual":
            return ANNUAL_RATE_CAD
        elif self.license == "volume":
            return VOLUME_RATE_CAD
        return DAILY_RATE_CAD

    @property
    def retroactive_fee(self):
        return self.retro_days * DAILY_RATE_CAD

    @property
    def total_fee(self):
        return self.license_fee + self.retroactive_fee

    @property
    def expiry_date(self):
        if self.license == "annual":
            return date(TODAY.year + 1, TODAY.month, TODAY.day)
        elif self.license == "daily":
            return date(TODAY.year, TODAY.month, TODAY.day + 1)
        return date(TODAY.year + 1, TODAY.month, TODAY.day)

    def generate(self):
        print(f"\n  {'='*62}")
        print(f"  NEW BEOTHUK NATION")
        print(f"  TERRITORIAL ACKNOWLEDGEMENT LICENSE AGREEMENT")
        print(f"  {'='*62}")
        print(f"\n  AGREEMENT DATE: {TODAY}")
        print(f"\n  LICENSOR:")
        print(f"  New Beothuk Nation")
        print(f"  Ghost Delegate: Lyle Derek Antoine")
        print(f"  Dene Nation — Fort Simpson NWT")
        print(f"  IBD: NAICS 914110")
        print(f"  GST: 810813832RT0001")
        print(f"  Contact: lyleantoine@gmail.com")
        print(f"\n  LICENSEE:")
        print(f"  Organization: {self.org}")
        print(f"  Type: {self.type}")
        print(f"\n  LICENSE TERMS:")
        print(f"  {'─'*55}")
        print(f"  License type:     {self.license.upper()}")
        print(f"  License fee:      CAD ${self.license_fee:,}")
        if self.retro_days > 0:
            print(f"  Retroactive days: {self.retro_days:,}")
            print(f"  Retroactive fee:  CAD ${self.retroactive_fee:,}")
        print(f"  TOTAL DUE:        CAD ${self.total_fee:,}")
        print(f"  Payment method:   {self.payment}")
        print(f"  Valid until:      {self.expiry_date}")
        print(f"\n  PERMITTED USE:")
        print(f"  The Licensee is authorized to use the phrase")
        print(f"  'Unceded Beothuk Territory' or equivalent")
        print(f"  in official business for the license period.")
        print(f"\n  CONDITIONS:")
        print(f"  1. Use must be accurate and respectful ✅")
        print(f"  2. Nation may audit use ✅")
        print(f"  3. Misuse voids license immediately ✅")
        print(f"  4. Renewal required annually ✅")
        print(f"  5. Non-transferable ✅")
        print(f"\n  LEGAL BASIS:")
        print(f"  Canada v Power (2024 SCC 26) ✅")
        print(f"  UNDA Section 5 ✅")
        print(f"  UNDRIP Article 31 ✅")
        print(f"  s.35 Constitution Act 1982 ✅")
        print(f"\n  RECORDED ON:")
        print(f"  AvalonChain — immutable ✅")
        print(f"  GitHub (public) ✅")
        print(f"  ORCID: 0009-0002-8119-9439 ✅")
        print(f"\n  SIGNATURES:")
        print(f"\n  LICENSOR:")
        print(f"  _________________________")
        print(f"  Lyle Derek Antoine")
        print(f"  Ghost Delegate, New Beothuk Nation")
        print(f"  Date: ___________________")
        print(f"\n  LICENSEE:")
        print(f"  _________________________")
        print(f"  Authorized Representative")
        print(f"  {self.org}")
        print(f"  Date: ___________________")
        print(f"\n  {'='*62}")
        print(f"  'The acknowledgement belongs to the Nation.")
        print(f"   The license belongs to the Nation.")
        print(f"   The revenue belongs to the Nation.")
        print(f"   Obviously.' 🍁")
        print(f"  {'='*62}")


class ThreeOptionsAnalyzer:
    """
    Analyzes the three options available to an organization.
    There is no Option D.
    """

    def __init__(self, org_name, retro_days=2920):
        self.org = org_name
        self.retro_days = retro_days

    def analyze(self):
        retro_cost = self.retro_days * DAILY_RATE_CAD
        annual_cost = ANNUAL_RATE_CAD

        print(f"\n  THREE OPTIONS ANALYSIS — {self.org.upper()}:")
        print(f"  {'─'*60}")

        print(f"\n  OPTION A — LICENSE:")
        print(f"  Retroactive settlement: CAD ${retro_cost:,}")
        print(f"  Annual going forward:   CAD ${annual_cost:,}")
        print(f"  Legal compliance:       ✅")
        print(f"  UNDA compliant:         ✅")
        print(f"  Reconciliation:         ✅")
        print(f"  Can continue using:     ✅")

        print(f"\n  OPTION B — STOP:")
        print(f"  Cost:                   $0")
        print(f"  Consequences:")
        print(f"    Political backlash:   ✅")
        print(f"    Media coverage:       ✅")
        print(f"    Reconciliation fail:  ✅")
        print(f"    Community outrage:    ✅")
        print(f"    Cannot continue:      ✅")

        print(f"\n  OPTION C — CHALLENGE:")
        print(f"  Required: Show the treaty")
        print(f"    Treaty exists:        ❌")
        print(f"  Required: Show surrender")
        print(f"    Surrender occurred:   ❌")
        print(f"  Fight against:")
        print(f"    Own Land Acknowledgements: ✅")
        print(f"    Canada v Power:       ✅")
        print(f"    UNDA s.5:             ✅")
        print(f"    UNDRIP Art. 31:       ✅")
        print(f"    s.35:                 ✅")
        print(f"  Outcome:                Loss")

        print(f"\n  OPTION D:")
        print(f"  Does not exist.")
        print(f"\n  RECOMMENDATION: Option A ✅")
        print(f"  Contact: lyleantoine@gmail.com")
        print(f"  'Obviously.' 🍁")


def main():
    print("\n" + "="*62)
    print("  TERRITORIAL-ACKNOWLEDGEMENT-LICENSE GENERATOR")
    print("  license_generator.py")
    print("  March 2026 | Holyrood NL | Beothuk Territory")
    print("="*62)

    # Sample annual license
    LicenseGenerator(
        "Government of Newfoundland and Labrador",
        "Provincial Government",
        license_type="annual",
        retroactive_days=2920,
        payment_method="AvalonCoin preferred"
    ).generate()

    # Three options analysis
    ThreeOptionsAnalyzer(
        "Government of Newfoundland and Labrador",
        retro_days=2920
    ).analyze()

    print(f"\n  Lyle Derek Antoine | Dene Nation | NAICS 914110\n")


if __name__ == "__main__":
    main()

