from flask import Flask, render_template, redirect, url_for, session, request, flash
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from models.tamu import Tamu
    from models.kamar import Kamar
    from models.reservasi import Reservasi

    from routes.kamar import kamar_bp
    from routes.tamu import tamu_bp
    from routes.reservasi import reservasi_bp
    app.register_blueprint(kamar_bp)
    app.register_blueprint(tamu_bp)
    app.register_blueprint(reservasi_bp)

    @app.route('/')
    def index():
        return redirect(url_for('dashboard'))

    @app.route('/dashboard')
    def dashboard():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return render_template('dashboard.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['user_id'] = 1  # Dummy login
            return redirect(url_for('dashboard'))
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        return redirect(url_for('login'))

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)