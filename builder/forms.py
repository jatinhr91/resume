from django import forms

class ResumeForm(forms.Form):
    name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email Address', required=False)
    phone = forms.CharField(label='Phone Number', max_length=15, required=False)
    summary = forms.CharField(label='Professional Summary', widget=forms.Textarea, required=False)
    education = forms.CharField(label='Education', widget=forms.Textarea, required=False, help_text="Enter degrees, institutions, and graduation years.")
    skills = forms.CharField(label='Skills', widget=forms.Textarea, required=False, help_text="Separate skills by commas (e.g., Python, Django, HTML).")
    experience = forms.CharField(label='Experience', widget=forms.Textarea, required=False, help_text="Mention roles, responsibilities, and achievements.")

