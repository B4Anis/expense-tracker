# Personal Expense Tracker - Sprint 1 Documentation

## Project Overview

**Project Name:** Personal Expense Tracker  
**Description:** The Personal Expense Tracker is a desktop application aimed at helping users track their personal expenses. The application stores expense records in a local embedded database and provides functionalities such as adding, editing, and deleting expenses, while maintaining data persistence across sessions.

## Sprint Overview

### Sprint 1 - Refactoring & Core Features
**Sprint Duration:** 180 minutes  
**Sprint Goal:** Refactor the existing monolithic code, enhance code quality by applying object-oriented programming (OOP) principles, integrate an embedded database, add input validations, and implement the ability to delete an expense entry.

---

## Features Implemented in Sprint 1

### 1. **Refactoring the Code into Smaller Modules/Classes**

- **Description:** The monolithic code provided was refactored into smaller, manageable modules, following OOP principles like encapsulation, inheritance, and polymorphism.
- **Approach:**
  - Separated responsibilities into distinct classes (e.g., `Expense`, `ExpenseManager`, `DatabaseHandler`, etc.).
  - Applied OOP principles to ensure each class is modular, reusable, and maintainable.
  - Improved the code structure to increase readability and future scalability.
- **Outcome:** The code is now well-organized and ready for future feature additions.

---

### 2. **Improved Use of OOP Principles**

- **Description:** Enhanced the use of OOP in the project to make the code easier to manage, extend, and test.
- **OOP Principles Applied:**
  - **Encapsulation:** Grouped related data and behavior in classes (e.g., an `Expense` class for expense data).
  - **Abstraction:** Defined abstract behaviors for common operations (e.g., managing expenses).
  - **Inheritance:** Shared functionality between classes where appropriate (e.g., handling different types of transactions).
- **Outcome:** Code now follows best practices of OOP, improving maintainability and reducing redundancy.

---

### 3. **Input Validation and Data Checks**

- **Description:** Introduced input validation to prevent erroneous data from being saved into the system, including duplicate entries or invalid formats (e.g., date, amount).
- **Validations Added:**
  - **Duplicate Checks:** Ensured that no duplicate expense entries are allowed.
  - **Input Validation:** Validated that the date format, description, and expense amount are correct.
- **Outcome:** Users can now enter valid expense data without concerns about duplicates or improper formats.

---

### 4. **Embedded Database Integration**

- **Description:** Integrated a lightweight embedded database (SQLite) for local data storage. All expense entries are stored and retrieved from this database, ensuring data persists between sessions.
- **Steps Taken:**
  - Configured SQLite to manage all expense data.
  - Implemented CRUD operations (Create, Read, Update, Delete) to handle expenses.
  - Migrated data management logic to use the database.
- **Outcome:** Expense data is now stored locally and is persistent, ensuring users do not lose their data when the application is closed.

---

### 5. **Delete Expense Option**

- **Description:** Added a feature allowing users to delete an expense entry. Before deletion, users are prompted for confirmation to avoid accidental deletions.
- **Steps Taken:**
  - Implemented a `deleteExpense` method in the `ExpenseManager` class.
  - Added a confirmation prompt before deletion.
  - Ensured the deletion is reflected in the embedded database.
- **Outcome:** Users can now delete unwanted or erroneous expense entries with ease, and the data is correctly removed from the database.

---

## Sprint 1 Task Breakdown

| **Task**                              | **Description**                                                                 | **Assigned To**    | **Est. Time** | **Actual Time** | **Status** |
|---------------------------------------|---------------------------------------------------------------------------------|--------------------|---------------|-----------------|------------|
| Refactor Code into Smaller Modules    | Break the monolithic code into smaller, manageable modules/classes.              | [Team Member 1]     | 60 mins       | 55 mins         | Done       |
| Apply OOP Principles                  | Apply OOP concepts like inheritance and encapsulation to improve code structure. | [Team Member 1]     | 30 mins       | 25 mins         | Done       |
| Input Validation & Data Checks        | Add validation for expense entries (e.g., duplicate checks, proper format).      | [Team Member 2]     | 30 mins       | 35 mins         | Done       |
| Integrate Embedded Database           | Integrate SQLite for local data storage, and migrate the expense logic.          | [Team Member 3]     | 45 mins       | 50 mins         | Done       |
| Implement Delete Expense Option       | Add delete functionality for expenses, including database integration.           | [Team Member 2]     | 15 mins       | 15 mins         | Done       |

---

## Definition of Done (DoD) for Sprint 1

- **Refactoring:** The codebase is modular, and each module follows object-oriented design principles.
- **Database Integration:** Expense data is stored in an embedded database, and CRUD operations (Create, Read, Update, Delete) work correctly.
- **Delete Functionality:** Users can delete expenses, and the deletion is confirmed via prompt.
- **Input Validation:** Proper checks and validations are in place to avoid invalid or duplicate expense entries.
- **Testing:** All functionalities have been tested and are working as expected, with no critical bugs.

---

## Challenges Encountered

- **Complexity of Refactoring:** The existing monolithic code was difficult to break down into smaller pieces. Careful planning was required to ensure that the refactoring did not introduce new bugs.
- **Database Migration:** Integrating the embedded database and migrating the existing data handling posed a challenge, particularly ensuring no data loss and smooth retrieval.

---

## Next Steps

In the next sprint, we will focus on:

1. Adding a feature for users to edit existing expense entries.
2. Implementing more complex reports and filtering of expenses.
3. Enhancing the user interface to improve user experience.
4. Addressing any minor bugs or performance issues that arise during further testing.

---

## Conclusion

Sprint 1 was successfully completed, with all planned tasks delivered on time and as expected. The Personal Expense Tracker now has a cleaner, more maintainable codebase, an integrated embedded database, and core functionality enhancements, setting the stage for future feature development and improvements.
