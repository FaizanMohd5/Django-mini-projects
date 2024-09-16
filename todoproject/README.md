### **Project Overview**
We created a **to-do list app** using **Django** for both the backend and frontend. The app allows users to:
- Add tasks with titles and descriptions.
- View all tasks, both completed and incomplete.
- Mark tasks as completed or incomplete.
- Edit tasks.
- Delete tasks.
- Filter tasks by status (completed or incomplete).

The design was tailored for both desktop and mobile users, ensuring a responsive interface that works seamlessly across devices.

---

### **Step-by-Step Development Journey**

#### 1. **Project Setup**
- We set up the Django project with a basic structure, including models, views, templates, and static files.
- **Models:** Defined the `Task` model with fields for `title`, `description`, `completed`, and timestamps.
- **Database Migration:** Ran migrations to create the database schema for tasks.

#### 2. **Adding Tasks**
- **Form Setup:** We created a form to add tasks. This form included a title and description input, with a submit button.
- **Views:** The `add_task` view handled creating new tasks.
- **Templates:** The HTML form was displayed on the main page (`home.html`), inside the **"Add Task"** section.

#### 3. **Displaying Tasks**
- **Task List:** We displayed tasks in a list format next to the form in a grid-like layout for desktop.
- Each task had options to **edit**, **delete**, or **mark as complete/incomplete**.
  
#### 4. **Edit and Delete Tasks**
- **Edit Functionality:** A separate page (`update.html`) allowed users to edit the title and description of tasks.
- **Delete Option:** We added a delete button next to each task on the task list to remove it from the database.

#### 5. **Marking Tasks as Completed/Incomplete**
- **Views and URL Routing:** We added routes to toggle a task's `completed` status. Users could click buttons to mark tasks as either completed or incomplete, which updated the task's appearance.
  
#### 6. **Task Filtering**
- **Status Filtering:** On the home page, we added filter options to view **completed** and **incomplete** tasks.
- **Buttons to Filter Tasks:** We initially used buttons to filter tasks by their status, then switched to **divs** styled like buttons for a better interface look.

#### 7. **Styling**
- **CSS Layout and Styling:** 
  - We added custom CSS to create a modern, **dark-themed UI** inspired by Discord.
  - Used `flexbox` for layout management, making the interface dynamic.
  - Styled the form, task list, and buttons for a cohesive look.
  
#### 8. **Responsiveness**
- We ensured the app was **responsive**, using media queries to adjust layouts for mobile screens.
  - **Mobile Design:** On mobile devices, the task form and task list were displayed **vertically** for better usability, with the task form on top and the list below.
  - Adjusted padding, margins, and widths for optimal viewing on small screens.
  
#### 9. **Refining the UI**
- We went back and forth on the **positioning of elements** like the task form and task list. Initially side-by-side, we switched to a **vertical layout for mobile** to enhance user experience.
  
---

### **The Final Interface**

#### **Desktop View:**
- The main page has a **two-column layout**:
  - On the left: **Add Task Form** with fields for title and description.
  - On the right: **Task List** showing all tasks.
- Tasks can be marked as completed/incomplete, edited, or deleted.
- Filter options (completed/incomplete) are prominently displayed at the top of the task list.

#### **Mobile View:**
- The layout becomes **vertical** on smaller screens, with the **Add Task Form** on top and the **Task List** below.
- Buttons and links are touch-friendly, with adequate spacing and large tap targets.
  
---

### **Reflection: What We Did Right & Areas for Improvement**

#### **Strengths:**
- **Clean and Simple UI:** The interface is easy to navigate, with a modern look and feel.
- **Responsive Design:** The app works well on both desktop and mobile devices, adjusting layout and element sizes dynamically.
- **Functionality:** All essential to-do app features are included: adding, editing, deleting and filtering tasks.
- **User Experience:** The task form and list are intuitive to use, with smooth transitions between completed and incomplete tasks.
  
#### **Possible Improvements:**
- **Error Handling:** We could add more detailed error messages or form validation (e.g., alerting users if they submit an empty task).
- **UI Tweaks:** Additional design enhancements, such as animations when marking tasks as completed, could further improve user experience.
- **Sorting Options:** A future improvement could include the ability to sort tasks by date or priority.
  
---

### **Conclusion**

This **Django To-Do List** app is a great starting project that covers essential CRUD functionality, user interaction, and responsive design. We made a conscious effort to ensure the UI is both visually appealing and functional, especially on mobile devices. 
