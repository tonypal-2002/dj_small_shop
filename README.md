# dj_small_shop

## Setup Instruction

### Prerequisites

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/)
 
## Go to Terminal

1. **Install Django Framework**
```
pip install django
```
2. **Install Pillow Library**
```
pip install pillow
```
3. **Install PDF Library**
```
pip install xhtml2pdf
```

4. **Install Django Cross-Origin Resource Sharing (CORS)**
```
pip install django-cross-headers
```
5. **Project Setup**
```
django-admin startproject config .
```
6. **Create Backend App**
```
python manage.py startapp backend
```
7. **Create API V1 App**
```
python manage.py startapp api_v1
```
8. **Create API V2 App**
```
python manage.py startapp api_v2
```