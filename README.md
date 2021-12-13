# Boostcamp-CV-Serving

## Prerequisites
- MySQL
- GCP Cloud Storage
  - GCP key file
- Sentry
- Streamlit Cloud
- Secrets: `.streamlit/secrets.toml`
  ```
    [mysql]
    host = <YOUR_HOST>
    port = 3306
    database = <YOUR_DATABASE>
    user = <YOUR_USER>
    password = <YOUR_PASSWORD>

    [gcp]
    project_id = <YOUR_PROJECT_ID>
    private_key_id = <YOUR_PROJECT_KEY>
    private_key = <YOUR_PRIVATE_KEY>
    client_email = <YOUR_CLIENT_EMAIL>
    client_id = <YOUR_CLIENT_ID>
    bucket = "<YOUR_BUCKET>"

    [sentry]
    sentry_url = <YOUR_SENTRY_URL>
  ```