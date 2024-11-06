import dashboard

# Dashboard entrypoint
if __name__ == '__main__':
    # Run web server on localhost:1234
    dashboard.app.run(host='0.0.0.0', port=1234)