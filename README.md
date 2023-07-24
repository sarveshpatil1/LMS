![logo](https://github.com/sarveshpatil1/LMS/assets/50295990/5a2443a4-aac6-4d7f-b839-85e41ac39980)


We are building an E-Learning platform where the authors can post their own courses and students can create their account to learn the published courses.

## The Home page

https://github.com/sarveshpatil1/LMS/assets/50295990/69841467-7cb7-4903-97d7-dd4ee8b54499

## Login, Signup, Forgot Password

https://github.com/sarveshpatil1/LMS/assets/50295990/030d64a9-a357-4bab-be5a-411c984a247c

## Gold Tier Student Enrollment to the course with access to discounted rates

https://github.com/sarveshpatil1/LMS/assets/50295990/a7baa601-be6b-41f7-b2ed-8acfff53e4f7

## Free Tier student login and watching a lesson

https://github.com/sarveshpatil1/LMS/assets/50295990/9f9ab799-ce00-471d-9d98-8143a12a8b11

## User Registration (Instructor)

https://github.com/sarveshpatil1/LMS/assets/50295990/a2cfdcb4-fe3a-451a-a512-c23148410f2b

## Instructors can create personalized courses and post them on the platform

https://github.com/sarveshpatil1/LMS/assets/50295990/3c3a56e1-9c8e-4ddc-9ba9-3356081a8be6


<br>
<br><br>
<br>



## Some Important features of the project:
  •	There are 3 types of registrations Instructor, Free tier student, and Gold tier student.
  
  •	Free student will not have any discounts accessible to them
  
  •	Gold students will be able to buy the courses with additional discounts. Gold students must pay 199 to be a member for lifetime.
  
  •	Only enrolled students can view the videos.
  
  •	Preview video can be seen if only the author/instructor is set it as preview for free.
  
  •	All student accounts can register to free courses.
  
  •	Authors can register and post their own courses, create new courses, change and upload video urls and images.


### To start this project follow the below instructions:
#### 1. After cloning to local please install the venv for Django by using this command : 
```
python3 -m venv venv
```
#### 2. Start the virtual environment by this command : 
```bash
venv\Scripts\Activate
```
#### 3. Install the dependencies by : 
```
pip install -r requirements.txt
```
#### 4.1 (optional). If you want to pre-load initial data you can do it by using data.json file run command : 
```
python manage.py loaddata data.json
```
#### 4. Once all  the dependencies are done start the project by using this cmd : 
```
python manage.py runserver
```
#### Note: We are using google's SMTP server so please do change the details accordingly in settings.py File
