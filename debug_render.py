
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.template.loader import render_to_string
from onlinecourse.models import Course

try:
    c = Course.objects.get(pk=1)
    # Simulate an authenticated user
    class MockUser:
        is_authenticated = True
        
    html = render_to_string('onlinecourse/course_detail_bootstrap.html', {'course': c, 'user': MockUser()})
    
    with open('debug_render.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Render successful. Output written to debug_render.html")
        
except Exception as e:
    print(f"Error: {e}")
