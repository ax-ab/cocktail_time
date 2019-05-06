# Generated by Django 2.2 on 2019-04-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('idDrink', models.AutoField(primary_key=True, serialize=False)),
                ('strDrink', models.CharField(max_length=30)),
                ('strTags', models.CharField(max_length=100)),
                ('strCategory', models.CharField(max_length=100)),
                ('strIBA', models.CharField(max_length=100)),
                ('strAlcoholic', models.CharField(max_length=100)),
                ('strGlass', models.CharField(max_length=100)),
                ('strInstructions', models.TextField()),
                ('strDrinkThumb', models.URLField()),
                ('strIngredient1', models.CharField(max_length=100)),
                ('strIngredient2', models.CharField(max_length=100)),
                ('strIngredient3', models.CharField(max_length=100)),
                ('strIngredient4', models.CharField(max_length=100)),
                ('strIngredient5', models.CharField(max_length=100)),
                ('strIngredient6', models.CharField(max_length=100)),
                ('strIngredient7', models.CharField(max_length=100)),
                ('strIngredient8', models.CharField(max_length=100)),
                ('strIngredient9', models.CharField(max_length=100)),
                ('strIngredient10', models.CharField(max_length=100)),
                ('strIngredient11', models.CharField(max_length=100)),
                ('strIngredient12', models.CharField(max_length=100)),
                ('strIngredient13', models.CharField(max_length=100)),
                ('strIngredient14', models.CharField(max_length=100)),
                ('strIngredient15', models.CharField(max_length=100)),
                ('strMeasure1', models.CharField(max_length=100)),
                ('strMeasure2', models.CharField(max_length=100)),
                ('strMeasure3', models.CharField(max_length=100)),
                ('strMeasure4', models.CharField(max_length=100)),
                ('strMeasure5', models.CharField(max_length=100)),
                ('strMeasure6', models.CharField(max_length=100)),
                ('strMeasure7', models.CharField(max_length=100)),
                ('strMeasure8', models.CharField(max_length=100)),
                ('strMeasure9', models.CharField(max_length=100)),
                ('strMeasure10', models.CharField(max_length=100)),
                ('strMeasure11', models.CharField(max_length=100)),
                ('strMeasure12', models.CharField(max_length=100)),
                ('strMeasure13', models.CharField(max_length=100)),
                ('strMeasure14', models.CharField(max_length=100)),
                ('strMeasure15', models.CharField(max_length=100)),
                ('dateModified', models.DateTimeField()),
            ],
        ),
    ]
