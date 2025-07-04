# Demo CI/CD Python Application

Demo aplikasi Python sederhana yang menunjukkan implementasi CI/CD pipeline dengan pengecekan unit test.

## 🚀 Fitur

- **Aplikasi Python**: Kelas Calculator dan fungsi greeting sederhana
- **Unit Testing**: Comprehensive test coverage menggunakan unittest
- **CI/CD Pipeline**: GitHub Actions workflow dengan multiple Python versions
- **Code Quality**: Linting dengan flake8 dan formatting dengan black
- **Code Coverage**: Laporan coverage menggunakan pytest-cov
- **Containerization**: Dockerfile dengan multi-stage build
- **Security**: Non-root user dalam container

## 📁 Struktur Project

```
demo-sesi-13/
├── app.py                    # Aplikasi utama
├── test_app.py              # Unit tests
├── requirements.txt         # Python dependencies
├── Dockerfile              # Container configuration
├── setup.cfg               # Flake8 dan pytest config
├── pyproject.toml          # Black configuration
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions workflow
└── README.md               # Documentation
```

## 🧪 Menjalankan Tests

### Menjalankan unit tests:
```bash
python -m unittest test_app.py -v
```

### Menggunakan pytest:
```bash
pip install -r requirements.txt
pytest test_app.py -v --cov=app
```

## 🔧 Development

### Setup environment:
```bash
# Install dependencies
pip install -r requirements.txt

# Run linting
flake8 .

# Run formatting check
black --check .

# Auto-format code
black .

# Run tests with coverage
pytest test_app.py -v --cov=app --cov-report=term
```

## 🐳 Docker

### Build image:
```bash
docker build -t demo-cicd-python:latest .
```

### Run container:
```bash
docker run demo-cicd-python:latest
```

## 🔄 CI/CD Pipeline

Pipeline GitHub Actions akan dijalankan pada:
- Push ke branch `main` atau `develop`
- Pull request ke branch `main`

### Stages:

1. **Test Stage**:
   - Setup Python environment (3.8, 3.9, 3.10, 3.11)
   - Install dependencies
   - Lint dengan flake8
   - Format check dengan black
   - Run unit tests dengan coverage
   - Upload coverage ke Codecov

2. **Build & Deploy Stage** (hanya untuk branch main):
   - Build aplikasi
   - Build Docker image
   - Deploy simulation

## 📊 Code Quality

- **Linting**: flake8 dengan aturan PEP 8
- **Formatting**: black dengan line length 127
- **Testing**: unittest dengan pytest runner
- **Coverage**: Target coverage > 80%

## 🛡️ Security

- Docker image menggunakan non-root user
- Multi-stage build untuk optimasi ukuran
- Health check untuk monitoring

## 🚀 Getting Started

1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest test_app.py -v`
4. Run application: `python app.py`

## 📈 Monitoring

Pipeline akan gagal jika:
- Unit tests tidak lulus
- Code coverage di bawah threshold
- Linting errors ditemukan
- Format code tidak sesuai standard

---

**Note**: Ini adalah demo untuk pembelajaran CI/CD. Dalam production, tambahkan konfigurasi deployment yang sesuai dengan environment kamu.
