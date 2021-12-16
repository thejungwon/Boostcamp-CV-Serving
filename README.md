# Boostcamp-CV-Serving

## Prerequisites
- MySQL
- GCP Cloud Storage
  - GCP key file
- Sentry
- Streamlit Cloud
- Secrets: `.streamlit/secrets.toml` 
  ```
    #DO NOT SHARE THIS INFORMATION!!!!
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
    bucket = <YOUR_BUCKET>

    [sentry]
    sentry_url = <YOUR_SENTRY_URL>
  ```

## Installation
### Local Environmnet
1. Add `secrets.toml` into `.streamlit` folder with the above information.
2. Install required libraries.
    ```
    pip install -r requirements.txt
    ```
4. Initialize Database.
    ```
    python init_database.py
    ```
5. Run following commands
    ```
    streamlit run main.py
    ```

### Streamlit Cloud Environment
1. Sign up for https://streamlit.io/cloud using Github account.
2. Click Deploy app.
3. Choose Github repository and main python file.
4. Copy and Paste the secrets by clicking the advanced setting button.
5. Deploy
