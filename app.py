from flask import Flask, render_template, redirect, url_for, session, request, flash
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Penting: import model SETELAH db.init_app agar context sudah benar
    from models.tamu import Tamu
    from models.kamar import Kamar
    from models.reservasi import Reservasi

    # Register blueprints
    from routes.kamar import kamar_bp
    from routes.tamu import tamu_bp
    from routes.reservasi import reservasi_bp
    from routes.dashboard import dashboard_bp
    from routes.api import api_bp
    app.register_blueprint(kamar_bp)
    app.register_blueprint(tamu_bp)
    app.register_blueprint(reservasi_bp)
    app.register_blueprint(dashboard_bp)  # TANPA url_prefix!
    app.register_blueprint(api_bp)

    # HAPUS/COMMENT route '/' di sini!
    # @app.route('/')
    # def index():
    #     return redirect(url_for('dashboard.dashboard'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['user_id'] = 1  # Dummy login
            return redirect(url_for('dashboard.dashboard'))  # redirect ke dashboard blueprint
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