from foodapp import App

if __name__ == '__main__':
    """calls flask App object
    Runs this file as the fast module
    Auto reloads when app is run
    """
    # App.config['TESTING']=False
    App.run(debug=True)
