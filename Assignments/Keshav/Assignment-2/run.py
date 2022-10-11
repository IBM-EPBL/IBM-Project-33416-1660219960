from project import apps

if __name__ == '__main__':

    apps.jinja_env.auto_reload = True
    apps.config['TEMPLATES_AUTO_RELOAD'] = True
    # apps.run(host='0.0.0.0', port=5000, debug=True)
    apps.run(debug=False)
