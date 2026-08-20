# Test Cases

## Test Case 1 – Normal Input

**Input:**
- Units: 50
- Late Payment: No

**Purpose:** Check normal bill calculation.

**Expected Result:** Bill should be calculated successfully.

**Status:** Passed


## Test Case 2 – Slab Boundary

**Input:**
- Units: 100
- Late Payment: No

**Purpose:** Check the calculation at the first slab boundary.

**Expected Result:** Bill should be calculated according to the applicable slab.

**Status:** Passed


## Test Case 3 – Multiple Slabs

**Input:**
- Units: 250
- Late Payment: Yes

**Purpose:** Check calculation when electricity consumption crosses multiple slabs.

**Expected Result:** Energy charge, fixed charge, and late fee should be calculated correctly.

**Status:** Passed


## Test Case 4 – Negative Units

**Input:**
- Units: -20

**Purpose:** Check whether negative electricity units are rejected.

**Expected Result:** Program should display an error message indicating that units cannot be negative.

**Status:** Passed


## Test Case 5 – Invalid Numerical Input

**Input:**
- Units: abc

**Purpose:** Check whether non-numeric input is handled correctly.

**Expected Result:** Program should display an error message asking the user to enter a valid number.

**Status:** Passed


## Test Case 6 – Invalid Late Payment Input

**Input:**
- Late Payment: maybe

**Purpose:** Check late-payment input validation.

**Expected Result:** Program should ask the user to enter only yes or no.

**Status:** Passed