import re

# Read the template file
with open('onlinecourse/templates/onlinecourse/course_detail_bootstrap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the split template variable by removing newlines within {{ }}
# This regex finds {{ followed by whitespace/newlines, then the variable name, then }}
content = re.sub(r'\{\{\s*\n\s*question\.question_text\s*\}\}', '{{ question.question_text }}', content)

# Write back
with open('onlinecourse/templates/onlinecourse/course_detail_bootstrap.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed split template variables!")
