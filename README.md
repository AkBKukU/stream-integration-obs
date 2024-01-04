# stream-integration-obs
Streaming service API integtration using OBS and Python

## Scene Data Storage

OBS uses the scene json file to store data related to scripts. Once you put in authentication information and connect to a service **your scene file should not be shared** as it could potentially be used to login to your accounts or abuse your API credentials.

TODO - Make a custom config file using `obs_frontend_get_current_profile_path` to store sensitive info in the profile folder.
