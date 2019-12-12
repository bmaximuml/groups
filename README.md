# Website Template
## Flask, Bulma

This is a website template created using Flask and Bulma.

This template uses SASS. After making changes to `static/sass/sass_styles.scss`,
run the command `sass --no-source-map sass/sass_styles.scss:sass_styles.css` to
regenerate the `static/sass_styles.css` file, which is looked at by the
application.

Much of the website can be configured using environment variables. These are laid out in the table below:

## Environment Variables

| Variable Name        | Purpose | Required / Optional |
| ---                  | ---     | ---                 |
| WFB_PROJECT_NAME     | This will be used for the title of the site, and the project name by the setuptools | Required |
| WFB_FLASK_SECRET_KEY | A secret key to be used by Flask for cryptographic functions | Required
| WFB_AUTHOR_NAME      | The name of the author of the site | Optional. If not specified, the WFB_PROJECT_NAME will be used
| WFB_AUTHOR_EMAIL     | The name of the author of the site | Optional
| WFB_PROJECT_URL      | The URL of the development site for the project, e.g. a hosted git repository | Optional
| WFB_SITE_URL         | The URL that this site will be hosted under | Optional
| WFB_SMTP_HOST        | The hostname to send emails through | Optional, however sending emails will be disabled if this is not specified
| WFB_SMTP_PORT        | The port to send emails through | Optional, however sending emails will be disabled if this is not specified
| WFB_SMTP_USERNAME    | The username to authenticate sending emails with | Optional, however sending emails with TLS will be disabled if this is not specified
| WFB_SMTP_PASSWORD    | The password to authenticate sending emails with | Optional, however sending emails with TLS will be disabled if this is not specified
| WFB_SMTP_TARGET      | The email address to send emails from the site to | Optional. If not specified, this will default to contactform@{WFB_SITE_URL}

## Install
1. `git clone https://github.com/benjilev08/groups`
2. `cd groups`
3. `pip3 install .`

## Setup

* `export WFB_FLASK_SECRET_KEY=<secret_key>`
    Set a secret key to be used by Flask. This must be set in order for the application to function. More detail on the Flask secret key can be found in [the Flask docs](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions).
* `export FLASK_APP=application.py`,
    Specify the file to be targeted by the Flask development web server
* `export FLASK_ENV=development` 
    Set the environment to development to use the Flask development web server 
