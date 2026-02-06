# User Story: Guest Checkout for Restricted Medication in Specific Region

## 1. Business Context

**Goal**: Enable users in specific regions (e.g., Valparaíso) to easily purchase restricted or location-dependent medications (e.g., Tramadol) via a Guest Checkout flow. This limits friction by not requiring immediate account creation while ensuring regional stock availability is respected.

## 2. User Story

**As a** Unregistered Customer (Guest)
**I want to** search for a specific medication after selecting my region (Valparaíso) and proceed to checkout
**So that** I can purchase my medication quickly without creating an account, while seeing correct availability for my location.

## 3. Acceptance Criteria (Gherkin)

### Scenario 1: End-to-End Purchase Flow for Tramadol in Valparaíso

> **QA Note**: This covers the critical path: Location Selection -> Search -> Add to Cart -> Guest Checkout.

**Given** the user is on the Salcobrand homepage
**And** the user has set their location to "Valparaíso"
**When** the user searches for "Tramadol"
**And** adds a random "Tramadol" product from the results to the cart
**And** proceeds to the cart and clicks "Ir a Pagar"
**Then** the user should be redirected to the identification page
**And** the user selects "Continúa como invitado"
**And** the user should see the "Información de cliente" form with the correct product in the order summary

## 4. Test Coverage (Functional & E2E)

The following test suite is limited to **3 key scenarios** to ensure focused coverage of the new feature.

### Test Case 1: E2E - Guest Checkout Initiation with Location Context

- **Type**: End-to-End
- **Priority**: Critical
- **Steps**:
  1.  Navigate to `www.salcobrand.cl`.
  2.  Handle any location popup by selecting "Valparaíso".
  3.  Search for "Tramadol".
  4.  Verify results appear.
  5.  Add the first available item to the cart.
  6.  Go to Cart -> Click "Ir a Pagar".
  7.  Select "Continúa como invitado".
  8.  **Assertion**: Verify URL contains `/checkout` or page title is "Información de cliente". Verify cart total > 0.

### Test Case 2: Functional - Location-Based Availability

- **Type**: Functional
- **Priority**: High
- **Steps**:
  1.  Set location to "Valparaíso".
  2.  Search for "Tramadol".
  3.  **Assertion**: Verify that the products displayed are available for purchase (stock check) in the selected region. (Contrast with out-of-stock behavior if applicable).

### Test Case 3: Functional - Cart Persistence and Data Integrity

- **Type**: Functional
- **Priority**: Medium
- **Steps**:
  1.  Add a product to the cart.
  2.  Navigate to the Cart page.
  3.  **Assertion**: Verify the Product Name, Price, and Quantity match what was selected in the search results.

---

_Document reviewed by QA Expert. Refinements made: Ensured "Guest" path is explicitly defined in Gherkin and Location prerequisite is a "Given" step to avoid flakiness._
