class Breed(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Breed must be greater than 1 character")]
    )
    age = models.PositiveIntegerField()
    sex = name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Sex must be greater than 1 character")]
    )

class Info(models.Model):
    date = models.DateField()
    location = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Info must be greater than 1 character")]
    )
    

class Animal(models.Model):
    species = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Species must be greater than 1 character")]
    )
    description = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(0, "Descriptions can be optional")]
    )
        breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)
    info = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)