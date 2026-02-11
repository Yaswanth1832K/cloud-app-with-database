
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from onlinecourse.models import Course, Lesson, Question, Choice

def populate_course():
    try:
        c = Course.objects.get(pk=1)
        print(f"Populating content for: {c.name}")
        
        # Create Lessons
        if c.lesson_set.count() == 0:
            Lesson.objects.create(title="Introduction to Cloud", order=0, course=c, content="Cloud computing is the on-demand availability of computer system resources, especially data storage (cloud storage) and computing power, without direct active management by the user.")
            Lesson.objects.create(title="Cloud Service Models", order=1, course=c, content="The three main service models of cloud computing are IaaS (Infrastructure as a Service), PaaS (Platform as a Service), and SaaS (Software as a Service).")
            Lesson.objects.create(title="Cloud Deployment Models", order=2, course=c, content="Deployment models include Public Cloud, Private Cloud, Hybrid Cloud, and Community Cloud.")
            print("Lessons created.")
            
        # Create Questions
        if c.question_set.count() == 0:
            # Q1
            q1 = Question.objects.create(course=c, question_text="What is Cloud Computing?", grade=10)
            Choice.objects.create(question=q1, choice_text="On-demand availability of computer system resources", is_correct=True)
            Choice.objects.create(question=q1, choice_text="A type of weather phenomenon", is_correct=False)
            Choice.objects.create(question=q1, choice_text="A hard drive attached to your computer", is_correct=False)
            
            # Q2
            q2 = Question.objects.create(course=c, question_text="Which of these is a Cloud Service Model?", grade=10)
            Choice.objects.create(question=q2, choice_text="HaaS (Hardware as a Service)", is_correct=False)
            Choice.objects.create(question=q2, choice_text="IaaS (Infrastructure as a Service)", is_correct=True)
            Choice.objects.create(question=q2, choice_text="TaaS (Testing as a Service)", is_correct=False)
            
             # Q3
            q3 = Question.objects.create(course=c, question_text="Which deployment model combines public and private clouds?", grade=10)
            Choice.objects.create(question=q3, choice_text="Hybrid Cloud", is_correct=True)
            Choice.objects.create(question=q3, choice_text="Community Cloud", is_correct=False)
            Choice.objects.create(question=q3, choice_text="Rain Cloud", is_correct=False)

            print("Questions created.")
            
    except Course.DoesNotExist:
        print("Course 1 not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    populate_course()
