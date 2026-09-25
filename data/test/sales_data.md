# Sample Sales Data for RAG

## 1. Sales Transactions

| Transaction ID | Date | Customer ID | Customer Name | Product ID | Product | Category | Region | Quantity | Unit Price (₹) | Discount (%) | Revenue (₹) | Sales Rep |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|
| TXN001 | 2026-01-05 | C001 | ABC Technologies | P001 | Laptop Pro 14 | Laptops | South | 5 | 85000 | 5 | 403750 | Ravi |
| TXN002 | 2026-01-07 | C002 | Global Solutions | P002 | Business Laptop 15 | Laptops | West | 3 | 72000 | 10 | 194400 | Priya |
| TXN003 | 2026-01-12 | C003 | Star Enterprises | P003 | Wireless Mouse | Accessories | South | 20 | 1500 | 5 | 28500 | Ravi |
| TXN004 | 2026-01-15 | C001 | ABC Technologies | P004 | Mechanical Keyboard | Accessories | South | 10 | 4500 | 0 | 45000 | Ravi |
| TXN005 | 2026-01-20 | C004 | TechWorld Ltd | P001 | Laptop Pro 14 | Laptops | North | 8 | 85000 | 8 | 625600 | Amit |
| TXN006 | 2026-02-03 | C005 | Digital India Pvt Ltd | P005 | 27-inch Monitor | Monitors | South | 12 | 28000 | 5 | 319200 | Priya |
| TXN007 | 2026-02-08 | C002 | Global Solutions | P003 | Wireless Mouse | Accessories | West | 50 | 1500 | 10 | 67500 | Priya |
| TXN008 | 2026-02-14 | C006 | FinServe Corp | P006 | USB-C Dock | Accessories | East | 15 | 8500 | 5 | 121125 | Amit |
| TXN009 | 2026-02-19 | C004 | TechWorld Ltd | P002 | Business Laptop 15 | Laptops | North | 6 | 72000 | 10 | 388800 | Amit |
| TXN010 | 2026-02-25 | C007 | Retail Mart | P004 | Mechanical Keyboard | Accessories | South | 25 | 4500 | 5 | 106875 | Ravi |
| TXN011 | 2026-03-02 | C001 | ABC Technologies | P005 | 27-inch Monitor | Monitors | South | 10 | 28000 | 10 | 252000 | Ravi |
| TXN012 | 2026-03-05 | C008 | Smart Systems | P001 | Laptop Pro 14 | Laptops | West | 4 | 85000 | 5 | 323000 | Priya |
| TXN013 | 2026-03-10 | C005 | Digital India Pvt Ltd | P006 | USB-C Dock | Accessories | South | 20 | 8500 | 8 | 156400 | Priya |
| TXN014 | 2026-03-15 | C009 | HealthCare Plus | P002 | Business Laptop 15 | Laptops | East | 10 | 72000 | 7 | 669600 | Amit |
| TXN015 | 2026-03-20 | C010 | EduTech Solutions | P005 | 27-inch Monitor | Monitors | North | 15 | 28000 | 5 | 399000 | Amit |

---

## 2. Product Knowledge

| Product ID | Product | Category | Description | Standard Price (₹) |
|---|---|---|---|---:|
| P001 | Laptop Pro 14 | Laptops | Premium 14-inch business laptop with 16GB RAM and 512GB SSD. | 85000 |
| P002 | Business Laptop 15 | Laptops | 15-inch enterprise laptop designed for business users. | 72000 |
| P003 | Wireless Mouse | Accessories | Ergonomic wireless mouse with USB receiver. | 1500 |
| P004 | Mechanical Keyboard | Accessories | Mechanical keyboard suitable for professional and gaming use. | 4500 |
| P005 | 27-inch Monitor | Monitors | 27-inch Full HD monitor suitable for office productivity. | 28000 |
| P006 | USB-C Dock | Accessories | Multi-port USB-C docking station for laptops. | 8500 |

---

## 3. Customer Information

| Customer ID | Customer | Industry | Region | Customer Type | Account Manager |
|---|---|---|---|---|---|
| C001 | ABC Technologies | IT Services | South | Enterprise | Ravi |
| C002 | Global Solutions | Consulting | West | Enterprise | Priya |
| C003 | Star Enterprises | Manufacturing | South | SMB | Ravi |
| C004 | TechWorld Ltd | Technology | North | Enterprise | Amit |
| C005 | Digital India Pvt Ltd | IT Services | South | Enterprise | Priya |
| C006 | FinServe Corp | Banking | East | Enterprise | Amit |
| C007 | Retail Mart | Retail | South | SMB | Ravi |
| C008 | Smart Systems | Technology | West | SMB | Priya |
| C009 | HealthCare Plus | Healthcare | East | Enterprise | Amit |
| C010 | EduTech Solutions | Education | North | SMB | Amit |

---

## 4. Sales Policies

### Discount Policy

- Enterprise customers can receive discounts up to **10%** without management approval.
- SMB customers can receive discounts up to **5%** without management approval.
- Discounts above these limits require Sales Manager approval.
- Discounts above **15%** require Regional Director approval.

### Volume Discount

| Quantity | Maximum Additional Discount |
|---|---:|
| 1–9 | 0% |
| 10–19 | 3% |
| 20–49 | 5% |
| 50+ | 8% |

### Refund Policy

- Customers can request a refund within **30 days** of purchase.
- Products must be unused and in original packaging.
- Enterprise customers may request an exception through their Account Manager.
- Refunds above ₹100,000 require Finance approval.

### Sales Escalation Policy

A sales transaction should be escalated when:

1. Discount exceeds the customer's permitted discount.
2. Transaction value exceeds ₹500,000.
3. Customer has multiple unusually large transactions within a short period.
4. Product availability is insufficient.
5. Customer requests special pricing outside the standard policy.

---

## 5. Example RAG Questions

### Basic Retrieval Questions

1. What is the standard price of Laptop Pro 14?
2. Which products belong to the Accessories category?
3. What is the refund period?
4. What is the maximum discount allowed for an SMB customer without approval?
5. Which region is ABC Technologies located in?

### Sales Analysis Questions

1. Which customer generated the highest revenue?
2. What are the top three products by revenue?
3. Which region generated the most sales?
4. How much revenue did ABC Technologies generate?
5. How many Laptop Pro 14 units were sold?
6. Which sales representative generated the highest revenue?

### Policy + Sales Reasoning Questions

1. Did any transaction exceed the standard discount allowed for the customer?
2. Which transactions require management approval?
3. Did any transaction exceed ₹500,000?
4. Should TXN015 require discount approval?
5. Which customers purchased more than 10 units in a single transaction?
6. Are there any transactions that require escalation?

---

## 6. Example Agentic RAG Workflow

```text
User Question
      │
      ▼
   AI Agent
      │
      ├──► Sales Data → SQL/Pandas
      │
      ├──► Product Data → Vector DB
      │
      ├──► Customer Data → Vector DB / SQL
      │
      └──► Sales Policies → RAG
                │
                ▼
          Combine Results
                │
                ▼
          LLM Reasoning
                │
                ▼
          Final Answer
```

### Example

**User:**

> "Can ABC Technologies receive a 12% discount on its next purchase?"

**Agent reasoning:**

```text
1. Identify customer → ABC Technologies
2. Customer type → Enterprise
3. Enterprise standard discount → 10%
4. Requested discount → 12%
5. Requested discount > standard limit
6. Check escalation policy
7. Management approval required
```

**Expected answer:**

> ABC Technologies is an Enterprise customer and can receive up to 10% discount without management approval. A 12% discount exceeds the standard limit, so Sales Manager approval is required.

---

## 7. Suggested RAG Metadata

For each document/chunk, store metadata such as:

```json
{
  "document_type": "sales_policy",
  "category": "discount",
  "source": "sales_policy.md",
  "date": "2026-01-01"
}
```

For sales records:

```json
{
  "document_type": "sales_transaction",
  "transaction_id": "TXN001",
  "customer_id": "C001",
  "product_id": "P001",
  "region": "South"
}
```

