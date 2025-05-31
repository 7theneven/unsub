# Email Unsubscribe System

A simple Flask-based email unsubscribe system that integrates with Airtable via Make.com (formerly Integromat). This system provides endpoints for users to unsubscribe and resubscribe from email communications, with the changes being automatically reflected in your Airtable database through Make.com automation.

## Features

- Simple unsubscribe/resubscribe endpoints
- Integration with Make.com webhooks
- Automatic database updates in Airtable
- Clean and minimal user interface
- Easy deployment on Render

## Technical Stack

- Python 3.x
- Flask web framework
- Make.com automation
- Airtable database
- Render deployment platform

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on `.env.example` and add your Make.com webhook URL:
   ```
   MAKE_WEBHOOK_URL=your_webhook_url_here
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Environment Variables

- `MAKE_WEBHOOK_URL`: Your Make.com webhook URL for automation
- `PORT`: (Optional) Port to run the application on (defaults to 5000) 