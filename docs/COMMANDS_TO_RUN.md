# Commands to Run Locally

Step-by-step commands to get the project running on your local machine.

## Prerequisites Check

Before starting, verify you have the required software:

```bash
# Check Python version (should be 3.8+)
python --version

# Check Node.js version (should be 18+)
node --version

# Check npm version
npm --version

# Check Git version
git --version
```

---

## First Time Setup

### Step 1: Navigate to Project Directory

```bash
cd hostel-project
```

### Step 2: Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (Command Prompt):
venv\Scripts\activate

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
# Follow the prompts to create username and password

# Start backend server
python manage.py runserver
```

**Backend is now running at:** http://localhost:8000

**Keep this terminal open!**

---

### Step 3: Frontend Setup (New Terminal)

Open a **new terminal window** and run:

```bash
# Navigate to project directory
cd hostel-project

# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Create environment file
# On Windows (Command Prompt):
copy .env.example .env

# On Windows (PowerShell) or macOS/Linux:
cp .env.example .env

# Start frontend server
npm run dev
```

**Frontend is now running at:** http://localhost:5173

**Keep this terminal open!**

---

## Daily Development Workflow

### Starting the Application

You need **two terminal windows** running simultaneously:

#### Terminal 1: Backend

```bash
cd hostel-project/backend
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux
python manage.py runserver
```

#### Terminal 2: Frontend

```bash
cd hostel-project/frontend
npm run dev
```

### Stopping the Application

In each terminal, press: **Ctrl + C**

---

## Accessing the Application

Once both servers are running:

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend** | http://localhost:5173 | Main application UI |
| **Backend API** | http://localhost:8000/api/ | REST API endpoints |
| **Admin Panel** | http://localhost:8000/admin/ | Django admin interface |

---

## Testing the Setup

### 1. Test Backend

Open browser and visit: http://localhost:8000/api/

You should see the Django REST Framework browsable API.

### 2. Test Admin Panel

Visit: http://localhost:8000/admin/

Login with the superuser credentials you created.

### 3. Test Frontend

Visit: http://localhost:5173/

You should see the Government Hostel Management System homepage.

### 4. Test Authentication

1. Click "Register here" or go to: http://localhost:5173/register
2. Fill in the registration form
3. After registration, login at: http://localhost:5173/login
4. You should be redirected to the dashboard

---

## Common Commands Reference

### Backend Commands

```bash
# Activate virtual environment
venv\Scripts\activate                    # Windows
source venv/bin/activate                 # macOS/Linux

# Start server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Create new app
python manage.py startapp appname
```

### Frontend Commands

```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Install new package
npm install package-name

# Run linter
npm run lint
```

---

## Troubleshooting

### Issue: Port Already in Use

**Backend (Port 8000):**
```bash
python manage.py runserver 8001
```

**Frontend (Port 5173):**
Vite will automatically use the next available port.

### Issue: Virtual Environment Not Activating (Windows PowerShell)

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Module Not Found (Backend)

```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### Issue: Dependencies Not Installing (Frontend)

```bash
# Clear cache and reinstall
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### Issue: CORS Errors

Check that backend CORS settings include frontend URL:
- File: `backend/config/settings/base.py`
- Should include: `http://localhost:5173`

### Issue: API Connection Failed

1. Ensure backend is running on port 8000
2. Check `.env` file in frontend has: `VITE_API_URL=http://localhost:8000/api`
3. Restart frontend server after changing `.env`

---

## Environment Variables

### Backend

Set environment for different configurations:

```bash
# Development (default)
set DJANGO_SETTINGS_MODULE=config.settings.dev

# Production
set DJANGO_SETTINGS_MODULE=config.settings.prod
```

### Frontend

Edit `frontend/.env`:

```env
VITE_API_URL=http://localhost:8000/api
```

---

## Quick Start (Copy-Paste)

### First Time Setup

**Terminal 1 (Backend):**
```bash
cd hostel-project/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Terminal 2 (Frontend):**
```bash
cd hostel-project/frontend
npm install
copy .env.example .env
npm run dev
```

### Daily Startup

**Terminal 1 (Backend):**
```bash
cd hostel-project/backend
venv\Scripts\activate
python manage.py runserver
```

**Terminal 2 (Frontend):**
```bash
cd hostel-project/frontend
npm run dev
```

---

## Verification Checklist

After setup, verify:

- [ ] Backend server starts without errors
- [ ] Frontend server starts without errors
- [ ] Can access http://localhost:8000/api/
- [ ] Can access http://localhost:8000/admin/
- [ ] Can access http://localhost:5173/
- [ ] Can login to admin panel
- [ ] Can register new user on frontend
- [ ] Can login on frontend
- [ ] No CORS errors in browser console

---

## Next Steps After Setup

1. **Explore the Admin Panel:**
   - Visit http://localhost:8000/admin/
   - Login with superuser credentials
   - Familiarize yourself with Django admin

2. **Test the Frontend:**
   - Register a new user
   - Login with credentials
   - Explore the dashboard

3. **Review Documentation:**
   - Read `README.md` for project overview
   - Check `docs/SETUP_GUIDE.md` for detailed setup
   - Review `docs/API_DOCUMENTATION.md` for API reference

4. **Start Development:**
   - Create new Django apps for features
   - Add new React components and pages
   - Implement CRUD operations

---

## Getting Help

If you encounter issues:

1. Check the error message carefully
2. Review the troubleshooting section above
3. Check documentation in `/docs` folder
4. Search for the error online
5. Ask team members for help

---

## Important Notes

- **Always activate virtual environment** before running Django commands
- **Keep both terminals running** during development
- **Don't commit `.env` files** to version control
- **Don't commit `venv/` folder** to version control
- **Commit frequently** with clear messages
- **Test before committing** your changes

---

*Happy Coding! 🚀*
