# Investment Management Project
## Overview
The Investment Management project is a Django-based backend system designed for managing and analyzing investment data. It allows users to upload investment-related data through Excel files, process it, and retrieve specific financial calculations. This system is built with Django Rest Framework, Django ORM, and Pandas, and is deployable via Docker.

## Features
- File Upload: API endpoints to upload trades.xlsx and cash_flows.xlsx files.
- Data Retrieval: Endpoints to retrieve calculated financial metrics like realized amount, remaining invested amount, gross expected amount, and closing date for a trade.

## Prerequisites
Before you begin, ensure you have the following installed:

- Python 
- Docker
- Git (for version control)

## Setup and Installation

1. Clone this repository to your local machine using git clone <repository-url>.
2. Build the Docker container using `docker build -t investment_project .`
3. Run the container using `docker run -p 8000:8000 investment_project`.
- The application will now be running on http://localhost:8000.



## Usage

### API Endpoints

1.  Upload Trades File:
- POST /upload/trades/
- Uploads a trades.xlsx file for processing.

2.  Upload Cash Flows File:
- POST /upload/cashflows/
- Uploads a cash_flows.xlsx file for processing.

3. Get Realized Amount for a Trade:
- GET /realized-amount/int:year/int:month/int:day
- Retrieves the realized amount for a specified trade.

4. Get Gross Expected Amount:
- GET /gross-expected-amount/int:year/int:month/int:day
- Retrieves the gross expected amount for a specified trade.

5. Get Remaining Invested Amount:
- GET /remaining-invested-amount/int:year/int:month/int:day
- Retrieves the remaining invested amount for a specified trade.

6. Get Closing Date for a Trade:
- GET /closing-date/str:trade_id
- Retrieves the closing date for a specified trade