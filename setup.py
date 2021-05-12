from distutils.core import setup
    
setup(
  name = 'googledrivepython',         
  packages = ['googledrivepython'],   
  version = '0.1.7',      
  license='MIT',        
  description = 'A python Google Drive API v3 wrapper',   
  author = 'Luyanda Dhlamini',                   
  author_email = 'luyanda.dhlamini@gmail.com',  
  url = 'https://github.com/luyandadhlamini',   
  download_url = 'https://github.com/luyandadhlamini/googledrivepython/archive/refs/tags/v0.1.7.tar.gz', 
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
    
    long_description='A python Google Drive API v3 wrapper',
    long_description_content_type='text/markdown'
)
