from django import forms
from .models import Report, Asset, ProblemType
from mptt.forms import TreeNodeChoiceField

class ReportForm(forms.ModelForm):
    asset = TreeNodeChoiceField(
        queryset=Asset.objects.all(),
        level_indicator='---', 
        empty_label="---------"
    )

    class Meta:
        model = Report
        fields = [
            'asset',
            'priority',
            'work_order_number',
            'problem_type',
            'problem_description',
            'recommended_action',
            'status',
            'previous_entry',
        ]
        widgets = {
            'priority': forms.Select(),
            'work_order_number': forms.TextInput(),
            'problem_type': forms.Select(),
            'problem_description': forms.Textarea(attrs={'rows': 4}),
            'recommended_action': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(),
            'previous_entry': forms.Select(),
        }

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'description', 'parent', 'priority']
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(attrs={'rows': 3}),
            'parent': forms.Select(),
            'priority': forms.Select(),
        }

class ProblemForm(forms.ModelForm):
    class Meta:
        model = ProblemType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(),
        }