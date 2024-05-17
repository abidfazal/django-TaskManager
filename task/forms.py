from django import forms 
from .models import Task,Catagory

design = 'w-full py-4 px-6 rounded-xl border'


        
        
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','catagory','priority','due_date')
        
        widgets = {
            'title':forms.TextInput(attrs={
                'placholder':'enter title',
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'description':forms.Textarea(attrs={
                'placholder':'enter description',
                'class': design
            }),
            'catagory':forms.Select(attrs={
                'placholder':'enter catagory',
                'class': design
            }),
            'priority':forms.Select(attrs={
                'placholder':'enter priority',
                'class': design
            }),
            'due_date':forms.TextInput(attrs={
                'placholder':'enter due date',
                'class': design
            }),
        #
        }
    
        
