from google.cloud import storage
from google.oauth2.service_account import Credentials

def main():
    # Define the service account key as a Python dictionary
    service_account_key = {
    "type": "service_account",
    "project_id": "ucsd-its-sandbox-ciops",
    "private_key_id": "eccb1dbb5b217671d5c79e58c6fcf31e2512239a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCfun9cZjGQUPCS\naiTtvWIv46Q7NLoAHFezsm/Qb+T3KWnZ9lqQy43A17AwS3twfopy5J6JghdQ4+8+\nEfKmi8s8oSI2v3Vi0AIZCVaZhFBCl1DvI2OfrkRJ6rehfEv5P5dsCScWitkRBvdr\nxXILo+HvBQMbbudvzT9RY4VcG0aWrnq3arVI8L4RMZhA3dVj4rQOj0xyjza3eEhP\nJ7kaehz3d7QDaCQMCQPQuqlJtGh1qomSl6P1fBLzwgEg6LXWwhrlMlvQWQOtCGv0\nZ/ka0/xyyblrk/VV0jR1YsWITtsMTgqg9LhwMME30PRC+PxIYQ8Pp62h1w5K04ET\nnhcAvd9XAgMBAAECggEAQZAHHBG0cXTPsoGQI+eTCG4rqMO1PztjAlcRT2DGfm9I\nzBczSHDNACVoZAJvqha+1Hcj3fSAhorw1iz+yT7jTsEjLo6667LO0aEEI2JsoVDD\n/0yq5U3eKOsHsei3tJjWGhnNqhKXE8akw19Ztw5vPDF1+4ozxC/euBUeFdb6S/mu\nUPKQT/o5rVxP2w1/VExl4IlvuWNbNXUQqDB0hrJwU/X0r8rvlx27Kq0ftXUBL3rS\nflq4kjy0yWLoiuWNTgfAE3vw0ZCSh6+H+5N1jaZOeRfiaXv6mr4YVP/b3rT2OvYg\nkyWol7jRcX8I3oMF2mUT0BAp4eYSHj9t/jf9v9O24QKBgQDhwzMmjjQCHlssKaav\nx08WaAKmQUOM7Krl8GQkPRHeIu2SITbi5buZbYfUQnIOiu7cApWIbZpUZmpvqCJL\nscfFOdBhF1A1Q1XKh2jWmaPXDf2Y5z5D65/z6AVhHarBmiJCS8TRLU8J+T2Bmd03\nUaf5gZsU96BMxjD5m7dkW19Z9wKBgQC1HyqWuROE1mDhmPwJNh/ACNVX+RItdwj0\n79ouZ0nBELDliWgUmO5UCLPxvTCYxOZl5X5N039o2szYnVdtCWTESaIgqRS4Wd8E\n2BsgYaRcbJVQ/tjb20Za6/KwbLUsNWZRii/1S2eVZB09RHx6VfN2JYPOUskojP/d\nfx/XHEFNoQKBgHzwlyU2O4gUnqZRIqNS7OzcgOLbaXPbIjUAlZsMhQ/nSoy9fu+Q\n7gJaAHqyjwaHUutFLtYCug8NYsgKR3iWmZUHis/ApC3l5tuflqB1BJwmbPsqtmXG\nR44nEJsPXQmpsF36KqEMrxo46hYIPcm4kfpeBKJU7EywvjfVOmf6vUk/AoGBAJ2B\nnOe1yuOaCmYlRAg+qR22kNEQKF6hRYi7jGEOMXVTroHuHDTNSXSKnPF8NOalVDcI\ne+3yHrpwi/NT4NNRd++6mOMOJpaqkOcFh5GBWA2H39GvzaZj6arnxQTnhCYNygze\nvxXxnQKtLUA6boV0eWQk+5pRI92/wEI+atIGIEQBAoGACrq80lrKrnlZBZT367hg\nR+4lBx/7zdIM2WOxgs63EPXQaWeFAOLM5fslgX0aflXdUDlwt8KXoM5298ZtAZSr\n773oWLvbtI0JGBaLJzGip/7+1i7Ti8jHYotaOQGbDTXxpD7zOBecTkT9Ijdax7jh\njpAxAhilt5+U6n+JYC0Mo0U=\n-----END PRIVATE KEY-----\n",
    "client_email": "nick-test@ucsd-its-sandbox-ciops.iam.gserviceaccount.com",
    "client_id": "112799574592932065124",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/nick-test%40ucsd-its-sandbox-ciops.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

    # Authenticate using the service account key
    credentials = Credentials.from_service_account_info(service_account_key)
    client = storage.Client(credentials=credentials)

    # List buckets
    print("Listing buckets:")
    buckets = list(client.list_buckets())
    for bucket in buckets:
        print(bucket.name)

if __name__ == "__main__":
    main()
