from distutils.core import setup
version = '0.2.0'
setup(
  name = 'googledrivepython',         
  packages = ['googledrivepython'],   
  version = version,      
  license='MIT',        
  description = 'A python Google Drive API v3 wrapper',   
  author = 'Luyanda Dhlamini',                   
  author_email = 'luyanda.dhlamini@gmail.com',  
  url = 'https://github.com/luyandadhlamini',   
  download_url = 'https://github.com/luyandadhlamini/googledrivepython/archive/refs/tags/v{}.tar.gz'.format(version), 
  keywords = ['Python', 'Google Drive', 'drive', 'API', 'wrapper' ],   
  install_requires=[            
          'oauth2-client',
          'google-api-python-client'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
    
    long_description_content_type = 'text/markdown',
    long_description = """# googledrivepython
A python Google Drive API v3 wrapper that enables:
* **Uploading** of files to Google Drive
* **Listing** of all files & folders available to a service account.
* **Sharing** of files with a list of email addresses.

<details><summary><b>How To Use</b></summary>
 1. Install the module using pip:

    
    pip install googledrivepython
    

2. Import the module & instantiate the GoogleDrivePython class:
    ```sh
    import googledrivepython as gdp
    gdrive = gdp.GoogleDrivePython()
    ```

3. Store the full path to your [google service account](https://cloud.google.com/iam/docs/service-accounts) in a variable:
    ```sh
    service_account = '/Users/luyanda.dhlamini/Projects/client_secret.json'
    ```

4. Create service account credentials:
    ```sh
    # Create credentials using the create_credentials function
    credentials = gdrive.create_credentials(service_account_json_filename = service_account)
    
    # Overwrite the class's default credentials with the newly created credentials.
    gdrive.credentials = credentials
    ```
 

5. Create a test text file for demonstration purposes:
    ```sh
    # Create & save a text file into the local directory
    test_file = "test_file.txt"
    f = open(test_file, "w")
    f.write("This will be written to text file.")
    f.close()
    ```


6. Upload the text file created above to google drive:
    ```sh
    # The code below would be used if we wanted to upload the file to an exsting google drive folder.
    # parent_folder_id would be passed in as an argument into the upload_file_to_google_drive() function using the 'parent_id' argument.
    # parent_folder_id = '1czCX8xlhkPyxuDl3gnUbEqncVO000000'
     
    # Upload the text file created above to google drive, storing its file_id in a dictionary
    file_id_dict = gdrive.upload_file_to_google_drive(path=test_file)
 
    # View the returned file id info.
    print(file_id_dict)
    
    # Get the id from the newly created file dictionary object
    file_id = file_id_dict['id']
    ```
 
 7. Share the newly uploaded file with a list of email addresses. Give each recipient a [role](https://developers.google.com/drive/api/v3/ref-roles).
    ```sh
    # Write down the email address(es) to share the file with in a list.
    email_list = ['johnsmith@gmail.com', 'luyendedlamini@gmail.com', 'rajarsheem@gmail.com']
    
    # Share the file with the email address list & print out the returned dictionary.
    share_results = gdrive.share_google_drive_file(file_id=file_id, emails=email_list)
    print(share_results)
    ```
 
 8. View the 100 most recently created files & folders for the service account to check if the test_file.txt is there.
    ```sh
    # Get all files & folders available to the service account into a dictionary.
    all_files_dict = gdrive.list_files_in_google_drive()
    
    # Print & view the available file, folder names and ids.
    # The newly created text file should also appear in the output.
    print(all_files_dict)
    ``` 

</details>
 
<details><summary><b>Package Dependencies</b></summary>

* [oauth2-client](https://pypi.org/project/oauth2-client/)
* [google-api-python-client](https://pypi.org/project/google-api-python-client/)

</details>

<details><summary><b>Credits & Roadmap</b></summary>

* This code has been modified from the version found [here](https://gist.github.com/rajarsheem/1d9790f0e9846fb429d7).
* This code has been tested on V3 of the google drive api found [here](https://developers.google.com/drive/api/v3/about-sdk).
* The package's functionality will be expanded to include other google drive api functionality should the need arise.


</details>""",
)
