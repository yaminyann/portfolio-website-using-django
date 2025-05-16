from django.db import models 



class Skill_Category(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Skills Category'
        ordering = ['order']


class Skill(models.Model):
    category = models.ForeignKey(Skill_Category, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.category.name}"
    
    class Meta:
        ordering = ['name', 'category']


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_image/', blank=True, null=True)
    technologies = models.CharField(max_length=500, help_text='Comma separet list of technologies')
    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
    
    class Meta:
        ordering = ['order']


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text='Comma separate to list of technologies ')

    def __str__(self):
        return f"{self.title} - {self.company}"
    
    def get_techologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
    
    def get_period(self):
        if self.end_date:
            return f"{self.start_date} - {self.end_date}"
        return f"{self.start_date} - present" 
    
    class Meta:
        ordering = ['-start_date']



class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    messages = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.created_at} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']