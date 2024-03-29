from astro import create_app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0')




# if we dont use a if __name__ conditional, we need to set variables:
# >> set FLASK_APP=<script.py>   // to set variable for file
# >> set FLASK_DEBUG=1     // for debugging w/o quitting flask
# >> flask run
