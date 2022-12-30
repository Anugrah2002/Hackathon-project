from django import forms

from .models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"

    def clean_branch_code(self):
        return self.cleaned_data["branch_code"].upper()
