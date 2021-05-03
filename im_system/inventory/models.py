from django.db import models

class Order(models.Model):
    order_name=models.CharField(max_length=20)      
    invoice=models.FileField(upload_to='invoice')   
    grn=models.FileField(upload_to='grn')
    comment = models.TextField(blank=True)

    def __str__(self):        
        return self.order_name

class Employee(models.Model):

    location_choices = (('HQ','HQ'),('Shatila','Shatila'),('Tripoli','Tripoli'),('Bekaa','Bekaa'),('Nabaa','Nabaa'),('Other','Other'))
    employee_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20,blank=True)
    email = models.CharField(max_length=100,blank= True)
    location = models.CharField(max_length=100,choices = location_choices,blank= True)
    title = models.CharField(max_length=100,blank= True)
    department = models.CharField(max_length=100,blank= True)
    project = models.CharField(max_length=100, blank= True)

    def __str__(self):        
        return self.employee_name

class Laptop(models.Model):

    laptop_manufacturer_choices = (
        ('Lenovo', 'Lenovo'), ('Acer', 'Acer'), ('Macbook','Macbook'),('Dell', 'Dell')
       , ('HP', 'HP'), ('Asus', 'Asus'), ('Other', 'Other'))
    processor_choices = ( ('Core i3', 'Core i3'), ('Core i5', 'Core i5'),('Core i7', 'Core i7'),('Other','Other'))
    status_choices = ( ('Stock', 'Stock'),('in_use','in_use'),('Maintenance','Maintenance'),('Depreciated','Depreciated'))

    order_name = models.ForeignKey(Order,on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100,choices = laptop_manufacturer_choices)
    serial_number = models.CharField(max_length=100,unique=True)
    ram = models.IntegerField(blank=True)
    processor = models.CharField(max_length=100,choices = processor_choices,blank=True)
    generation = models.IntegerField(blank=True)
    handover_date = models.DateField(blank=True)
    status = models.CharField(max_length=20, blank=False, choices = status_choices,default='Stock')
    employee_name = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    comment = models.TextField(blank=True)

    def __str__(self):        
        return self.serial_number


class Mobile(models.Model):

    mobile_manufacturer_choices = (('Samsung', 'Lenovo'), ('Huawei', 'Huawei'), ('Nokia','Nokia'),('Other', 'Other'))
    status_choices = ( ('Stock', 'Stock'),('in_use','in_use'),('Maintenance','Maintenance'),('Depreciated','Depreciated'))

    order_name = models.ForeignKey(Order,on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100,choices = mobile_manufacturer_choices)
    serial_number = models.CharField(max_length=100,unique=True)
    handover_date = models.DateField(blank=True)
    status = models.CharField(max_length=20, blank=False, choices = status_choices,default='Stock')
    employee_name = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    comment = models.TextField(blank=True)

    def __str__(self):        
        return self.serial_number


class Tab(models.Model):

    tab_manufacturer_choices = (('Samsung', 'Lenovo'), ('Huawei', 'Huawei'), ('Lenovo','Lenovo'),('Other', 'Other'))
    status_choices = ( ('Stock', 'Stock'),('in_use','in_use'),('Maintenance','Maintenance'),('Depreciated','Depreciated'))

    order_name = models.ForeignKey(Order,on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100,choices = tab_manufacturer_choices)
    serial_number = models.CharField(max_length=100,unique=True)
    handover_date = models.DateField(blank=True)
    status = models.CharField(max_length=20, blank=False, choices = status_choices,default='Stock')
    employee_name = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    comment = models.TextField(blank=True)

    def __str__(self):        
        return self.serial_number

class Sim(models.Model):

    sim_stype_choices = (('VPN','VPN'),('DATA','DATA'))
    sim_status_choices = (('Stock','Stock'),('in_use','in_use'))
    sim_number = models.CharField(max_length=100,unique=True)
    line_number = models.CharField(max_length=100,unique=True)
    sim_type =  models.CharField(max_length=20, blank=False, choices = sim_stype_choices)
    status = models.CharField(max_length=20, blank=False, choices = sim_status_choices,default='Stock')
    employee_name = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    comment = models.TextField(blank=True)

    def __str__(self):        
        return self.line_number

class Other(models.Model):

    status_choices = ( ('Stock', 'Stock'),('in_use','in_use'),('Maintenance','Maintenance'),('Depreciated','Depreciated'))

    asset_type = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=20, blank=False, choices = status_choices,default='Stock')
    employee_name = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    comment = models.TextField(blank=True)

    def __str__(self):        
        return self.asset_type
