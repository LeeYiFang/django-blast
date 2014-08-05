from django.contrib import admin
from blast.models import *
from django.forms import ModelForm
from suit.widgets import AutosizedTextarea

class BlastQueryRecordAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'enqueue_date', 'dequeue_date', 'result_date', 'result_status')
    fields = ('task_id', 'enqueue_date', 'dequeue_date', 'result_date', 'result_status')
    readonly_fields = ('enqueue_date',)
    list_filter = ('enqueue_date', 'dequeue_date', 'result_date', 'result_status')
    search_fields = ('task_id',)
    ordering = ('-enqueue_date',) # descending
admin.site.register(BlastQueryRecord, BlastQueryRecordAdmin)

class BlastDbForm(ModelForm):
    class Meta:
        widgets = {
            'description': AutosizedTextarea(attrs={'rows': 10, 'class': 'input-xxlarge'}),
        }

class BlastDbAdmin(admin.ModelAdmin):
    form = BlastDbForm
    list_display = ('fasta_file', 'organism', 'type', 'description', 'title', 'is_shown')
admin.site.register(BlastDb, BlastDbAdmin)

class OrganismForm(ModelForm):
    class Meta:
        widgets = {
            'description': AutosizedTextarea(attrs={'rows': 10, 'class': 'input-xxlarge'}),
        }

class OrganismAdmin(admin.ModelAdmin):
    form = OrganismForm
    list_display = ('display_name', 'short_name', 'tax_id', 'short_description')

    def short_description(self, obj):
        if len(obj.description) < 100:
            return obj.description
        else:
            return obj.description[:100] + '...'
    short_description.short_description = 'description'
    class Media:
        css = {
            'all': ('blast/css/organism-admin.css',)
        }
        js = ('blast/scripts/organism-admin.js',)
admin.site.register(Organism, OrganismAdmin)

class BlastDbTypeAdmin(admin.ModelAdmin):
    list_display = ('molecule_type', 'dataset_type')
    pass
admin.site.register(BlastDbType, BlastDbTypeAdmin)

class SequenceForm(ModelForm):
    class Meta:
        widgets = {
            'sequence': AutosizedTextarea(attrs={'rows': 10, 'class': 'input-xxlarge'}),
        }

class SequenceAdmin(admin.ModelAdmin):
    form = SequenceForm
    list_display = ('id', 'blast_db', 'length')
admin.site.register(Sequence, SequenceAdmin)

class JbrowseSettingAdmin(admin.ModelAdmin):
    list_display = ('blast_db', 'url')
admin.site.register(JbrowseSetting, JbrowseSettingAdmin)