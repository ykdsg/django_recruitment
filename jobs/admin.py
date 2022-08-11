from django.contrib import admin

# Register your models here.
from jobs.models import Job


# 定义模型的一些策略
class JobAdmin(admin.ModelAdmin):
    # 编辑页不露出
    exclude = ('creator','created_date','modified_date')
    # 控制列表页上的显示
    list_display = ('job_name','job_type','job_city','creator','created_date','modified_date')

    # 保存的时候进行的操作
    def save_model(self, request, obj, form, change):
        obj.creator=request.user
        super(JobAdmin, self).save_model(request,obj,form,change)





admin.site.register(Job,JobAdmin)