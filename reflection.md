# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial design used four classes: Owner, Pet, Task, and Scheduler.

Owner stores the owner's name and multiple pets. Pet stores basic pet
information and its care tasks. Task represents an individual care activity
including its time, duration, priority, frequency, due date, and completion
status. Scheduler retrieves all tasks through Owner and is responsible for
organizing and managing the schedule.

4. **b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---
I originally considered allowing Scheduler to work directly with one Pet.
I changed this design so Scheduler receives an Owner and retrieves tasks
using Owner.get_all_tasks(). This supports multiple pets and prevents the
scheduler from being tied to only one animal.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---
My conflict detection only checks whether two incomplete tasks occur on the
same date at exactly the same time. It does not calculate whether task
durations overlap.

For example, a task from 08:00–08:30 and another task at 08:15 would not
currently be flagged. I chose this approach because exact-time comparison
is easy to understand and sufficient for a lightweight pet-care scheduler.
A future version could calculate start and end times to detect overlapping
intervals.

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

- I used AI throughout the project mainly for brainstorming, debugging, and checking my code. 
- At the beginning, I used it to help decide what classes I needed and how Owner, Pet, Task, and Scheduler should work together. 
- Later, I used AI to help with things like sorting tasks, recurring tasks, conflict detection, Streamlit session state, and writing pytest tests.

- The most helpful prompts were the ones where I asked about one specific problem 
- instead of asking AI to build everything at once. 
- For example, asking how the Scheduler should get tasks from all of the owner's pets 
- helped me understand why `Owner.get_all_tasks()` was useful. 
- I also found it helpful to ask AI to explain code line by line when I did not understand something.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

- One time I did not accept an AI suggestion exactly as 
- it was given was when working on the Streamlit UI. 
- I originally added the new backend-connected UI without removing the starter UI, 
- which caused duplicate Streamlit widgets and errors. Instead of just adding more fixes on top of it, 
- I removed the old placeholder UI and kept one simpler version that used my actual Owner, Pet, Task, and Scheduler classes.
- I verified AI suggestions by running the program instead of assuming the code was correct. 
- I used `python main.py` to check the scheduler output, `streamlit run app.py` to test the UI, 
- and `python -m pytest` to check the automated tests. 
- If something failed, I looked at the error and changed the code before continuing.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

- I tested the main behaviors of the PawPal+ system. 
- I tested whether a task can be marked complete, whether adding a task actually adds it to a pet, 
- whether tasks are sorted correctly by time, whether a daily recurring task creates another task for the next day, 
- and whether the scheduler detects two tasks scheduled at the same time.

- These tests were important because they check the main features 
- that the scheduler depends on. For example, if sorting does not work, 
- the daily schedule would be shown in the wrong order. 
- Testing recurrence and conflict detection was also important 
- because those features have more logic and are easier to accidentally break.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

- I would rate my confidence in the scheduler as 4 out of 5. 
- The main features work and I tested them both manually and with pytest.

- If I had more time, I would test more edge cases such as invalid time inputs, 
- duplicate pet names, pets with no tasks, and weekly recurring tasks. I would also improve conflict detection. 
- Right now it only detects tasks that start at exactly the same time. 
- For example, a 30-minute task starting at 8:00 and another task starting at 8:15 could overlap, 
- but the current system would not detect that.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

- The part I am most satisfied with is how the different classes work together. 
- Instead of putting all of the logic inside the Streamlit app, I separated the backend logic into `pawpal_system.py`. 
- The Owner manages pets, each Pet manages its tasks, and the Scheduler gets all of the tasks through the Owner. 
- This made the code easier to understand and also made it easier to test without running the UI.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

- If I had another iteration, I would improve the conflict detection and the way tasks are stored. 
- I would make conflict detection check the full duration of a task instead of only comparing exact start times.

- I would also add permanent storage, such as a database or a file. 
- Right now the app uses Streamlit session state, so the information can disappear after the session ends. 
- Saving the pets and tasks permanently would make the app feel more like a real application.


**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned from this project is that designing the system before building the UI makes the project much easier to manage. Having separate classes with clear responsibilities helped me understand where each piece of logic should go.

- I also learned that AI is more useful when I use it as a helper instead of just copying everything it generates. 
- I still need to understand the code, run it, test it, and decide whether the suggestion actually fits my project. 
- Asking smaller and more specific questions also helped me learn more than asking AI to complete the whole project at once.