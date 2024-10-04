## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Okiitr/Bookstore.git
   cd Bookstore
   python -m venv myvenv
   source myvenv/bin/activate # On Windows use `myvenv\Scripts\activate`
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
