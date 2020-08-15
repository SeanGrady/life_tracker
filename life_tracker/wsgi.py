from life_tracker.flask_app import create_app


app = create_app()


@app.shell_context_processor
def make_shell_context():
    context = {
        'session': app.session,
        'AppUser': AppUser,
    }
    return context


if __name__ == "__main__":
    app.run(host='0.0.0.0')
