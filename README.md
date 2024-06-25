# Flask Application with Concurrent UI and VAPI

![Application Screenshot](https://github.com/AnubhavChaturvedi-GitHub/Vapi_Ai/blob/main/Screenshot%202024-06-25%20223340.png)

This project demonstrates a Flask application that serves a basic UI and concurrently runs a Virtual API (VAPI) using threading. The UI is served using Flask's `render_template` function, and the VAPI logic is contained in `Brain/main.py`.

### How to Run

1. Ensure Python and Flask are installed (`pip install flask`).
2. Navigate to the project directory.
3. Run `python app.py`.
4. Access the UI at `http://localhost:5000`.

### Components

- **UI**: Renders `index.html` located in the `templates` folder. Accessible at the root URL (`/`).
- **VAPI**: Concurrently runs alongside the UI using threading. VAPI logic is defined in `Brain/main.py`.

### Folder Structure

```
your_project/
│
├── app.py
├── Brain/
│   └── main.py
└── templates/
    └── index.html
```

### Additional Notes

- Ensure that `index.html` in the `templates` folder is appropriately customized for your UI needs.
- Customize `Brain/main.py` to include your specific VAPI functionality.
